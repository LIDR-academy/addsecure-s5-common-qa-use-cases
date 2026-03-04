// Read inputs.jsonl and compute value = (a + b) * c, write results to output JSONL.
// Minimal JSON parsing without external libraries.

#include <cerrno>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

struct InputCase {
    std::string case_id;
    double a;
    double b;
    double c;
};

// Trim whitespace from both ends
static std::string trim(const std::string& s) {
    size_t start = s.find_first_not_of(" \t\r\n");
    if (start == std::string::npos) return "";
    size_t end = s.find_last_not_of(" \t\r\n");
    return s.substr(start, end - start + 1);
}

// Extract a string value for a given key from a JSON object string
static bool extract_string(const std::string& json, const std::string& key, std::string& out) {
    std::string search = "\"" + key + "\"";
    size_t pos = json.find(search);
    if (pos == std::string::npos) return false;
    pos = json.find(':', pos + search.size());
    if (pos == std::string::npos) return false;
    pos = json.find('"', pos + 1);
    if (pos == std::string::npos) return false;
    size_t end = json.find('"', pos + 1);
    if (end == std::string::npos) return false;
    out = json.substr(pos + 1, end - pos - 1);
    return true;
}

// Extract a numeric value for a given key from a JSON object string
static bool extract_number(const std::string& json, const std::string& key, double& out) {
    std::string search = "\"" + key + "\"";
    size_t pos = json.find(search);
    if (pos == std::string::npos) return false;
    pos = json.find(':', pos + search.size());
    if (pos == std::string::npos) return false;
    pos++;
    while (pos < json.size() && (json[pos] == ' ' || json[pos] == '\t')) pos++;
    size_t end = pos;
    while (end < json.size() && json[end] != ',' && json[end] != '}' && json[end] != ' ') end++;
    std::string num_str = json.substr(pos, end - pos);
    const char* cstr = num_str.c_str();
    char* endptr = nullptr;
    errno = 0;
    out = std::strtod(cstr, &endptr);
    if (endptr == cstr || *endptr != '\0') {
        return false;  // no digits consumed or trailing garbage
    }
    // errno == ERANGE with non-inf result means subnormal underflow — still valid
    if (errno == ERANGE && std::isinf(out)) {
        return true;  // overflow to ±inf, valid per contract
    }
    return true;
}

static double compute(double a, double b, double c) {
    return (a + b) * c;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <input.jsonl> <output.jsonl>" << std::endl;
        return 1;
    }

    std::string input_path = argv[1];
    std::string output_path = argv[2];

    std::ifstream fin(input_path);
    if (!fin.is_open()) {
        std::cerr << "Error: cannot open input file: " << input_path << std::endl;
        return 1;
    }

    std::vector<std::pair<std::string, double>> results;
    std::string line;
    int lineno = 0;

    while (std::getline(fin, line)) {
        lineno++;
        line = trim(line);
        if (line.empty()) continue;

        std::string case_id;
        double a, b, c;

        if (!extract_string(line, "case_id", case_id)) {
            std::cerr << "Error: missing 'case_id' at line " << lineno << std::endl;
            return 1;
        }
        if (!extract_number(line, "a", a)) {
            std::cerr << "Error: missing or invalid 'a' at line " << lineno << std::endl;
            return 1;
        }
        if (!extract_number(line, "b", b)) {
            std::cerr << "Error: missing or invalid 'b' at line " << lineno << std::endl;
            return 1;
        }
        if (!extract_number(line, "c", c)) {
            std::cerr << "Error: missing or invalid 'c' at line " << lineno << std::endl;
            return 1;
        }

        double value = compute(a, b, c);
        results.push_back({case_id, value});
    }
    fin.close();

    std::ofstream fout(output_path);
    if (!fout.is_open()) {
        std::cerr << "Error: cannot open output file: " << output_path << std::endl;
        return 1;
    }

    for (const auto& r : results) {
        fout << "{\"case_id\": \"" << r.first << "\", \"value\": ";
        if (std::isnan(r.second)) {
            fout << "\"NaN\"";
        } else if (std::isinf(r.second)) {
            fout << (r.second > 0 ? "\"+Inf\"" : "\"-Inf\"");
        } else {
            fout << std::setprecision(17) << r.second;
        }
        fout << "}" << std::endl;
    }
    fout.close();

    std::cout << "Wrote " << results.size() << " results to " << output_path << std::endl;
    return 0;
}
