CXX      ?= g++
CXXFLAGS ?= -std=c++17 -O2 -Wall -Wextra

SRC     = cpp/main.cpp
BIN     = cpp/run_cpp
OUT_PY  = out_py.jsonl
OUT_CPP = out_cpp.jsonl

.PHONY: build clean

build:
	$(CXX) $(CXXFLAGS) -o $(BIN) $(SRC)

clean:
	rm -f $(BIN) $(OUT_PY) $(OUT_CPP)
