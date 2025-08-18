#!/usr/bin/env bash
set -euo pipefail

python -m pip install --quiet python-sat

python - <<'PY'
from pkg_solver import PackageProblem, UnsatisfiableError

packages = ['A', 'B', 'C']
requires = {'A': ['B']}
conflicts = {'B': ['C']}
problem = PackageProblem(packages, requires, conflicts)

# Satisfiable request
solution = problem.solve(['A'])
assert solution['A'] and solution['B'] and not solution['C']

# Unsatisfiable request exposes diagnostic
try:
    problem.solve(['A', 'C'])
    raise SystemExit('unexpected satisfiable result')
except UnsatisfiableError as exc:
    print(exc)
PY
