# Common Use Cases in Quality Assurance

## Problem statement

Python and C++ represent floating point numbers differently. E.g.: the number '-3' is represented as `-3` in C++ and as `-3.0` in Python. Therefore, for the same numerical inputs, the outcome of the formula `value = (a + b) * c` ends up being represented differently on each language.

## This repo

Implements a numeric equivalence validator between Python and C++ implementations of the formula `value = (a + b) * c` using IEEE 754 double-precision.

## Quick Start

```bash
# Install dependencies
python3 -m venv .venv/
source .venv/bin/activate
pip install -r requirements.txt

# Compile C++
make build

# Run all tests
make test
```

## Suites de Tests

| Suite | Comando | Descripcion |
|-------|---------|-------------|
| `all` | `pytest tests/ -v` | Todos los tests |
| `bdd` | `pytest -m bdd` | Escenarios Gherkin (15 casos) |
| `unit` | `pytest tests/unit/` | Unit tests de `normalize()` |
| `pbt` | `pytest tests/properties/ tests/test_properties.py` | Property-based tests (Hypothesis) |
| `playwright` | `pytest -m playwright` | E2E browser tests |
| `sync` | `pytest tests/test_sync.py` | Test de integracion |

## Makefile Targets

```bash
make build       # Compila cpp/run_cpp
make test        # Corre todos los tests
make pw-install  # Instala browsers de Playwright
make pw-test     # Corre tests Playwright
make pbt         # Corre property-based tests
make clean       # Limpia binarios y outputs
```

## Estructura del Proyecto

```
├── cpp/                  # Implementacion C++ de (a+b)*c
│   └── main.cpp
├── py/                   # Implementacion Python de (a+b)*c
│   └── run_py.py
├── tools/                # Oraculo de comparacion
│   └── compare.py        #   normalize() + reporte de diferencias
├── features/             # Escenarios Gherkin
│   └── sync_contract.feature
├── tests/
│   ├── bdd/              # BDD tests (pytest-bdd)
│   ├── unit/             # Unit tests de normalize()
│   ├── properties/       # PBT con Hypothesis
│   ├── e2e/              # E2E con Playwright
│   └── helpers/          # Helpers compartidos
├── scripts/              # Automatizacion
│   ├── syncguard_run.sh  #   Runner de suites con logging
│   └── syncguard_smoke.sh
├── prompts/              # Prompts usados para construir el proyecto
├── artifacts/syncguard/  # Logs de ejecucion
├── reports/syncguard/    # Reportes generados
├── .claude/              # Configuracion Claude Code + SyncGuard skill
└── .github/workflows/    # CI/CD con GitHub Actions
```

## SyncGuard

Agente automatizado que acelera el ciclo test-fix-verify:

```
/syncguard          # corre BDD por defecto
/syncguard all      # corre todos los tests
```

Flow: **run → triage → minimal fix → rerun (max 2 iterations) → report**
