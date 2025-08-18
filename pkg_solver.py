"""Package dependency solver using a SAT solver.

Encodes package requirements and conflicts as boolean formulas and
uses MiniSat to compute valid configurations. When the set of
requested packages has no satisfying assignment, a diagnostic
exception with an unsatisfiable core is raised.
"""
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Sequence

from pysat.formula import CNF
from pysat.solvers import Minisat22


class UnsatisfiableError(Exception):
    """Raised when the package constraints cannot be satisfied."""

    def __init__(self, core: Sequence[str]):
        self.core = list(core)
        msg = "No satisfying assignment; conflicting packages: " + ", ".join(self.core)
        super().__init__(msg)


@dataclass
class PackageProblem:
    """Represents a package constraint problem."""

    packages: Iterable[str]
    requires: Dict[str, Iterable[str]] = field(default_factory=dict)
    conflicts: Dict[str, Iterable[str]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.packages = list(self.packages)
        self.var_map = {pkg: i + 1 for i, pkg in enumerate(self.packages)}
        self.cnf = CNF()
        self._encode_constraints()

    def _encode_constraints(self) -> None:
        """Encode requirements and conflicts into CNF."""
        for pkg, deps in self.requires.items():
            for dep in deps:
                self.cnf.append([-self.var_map[pkg], self.var_map[dep]])
        for pkg, confs in self.conflicts.items():
            for conf in confs:
                self.cnf.append([-self.var_map[pkg], -self.var_map[conf]])

    def solve(self, requested: Sequence[str]) -> Dict[str, bool]:
        """Solve for a valid package configuration.

        Args:
            requested: Packages that must be installed.

        Returns:
            A mapping of package name to boolean indicating installation.

        Raises:
            UnsatisfiableError: if the requested packages cannot be satisfied.
        """
        solver = Minisat22(bootstrap_with=self.cnf.clauses)
        assumptions = [self.var_map[pkg] for pkg in requested]
        if solver.solve(assumptions=assumptions):
            model = set(solver.get_model())
            return {pkg: (var in model) for pkg, var in self.var_map.items()}
        core_vars = solver.get_core()
        core_pkgs = [pkg for pkg, var in self.var_map.items() if var in core_vars]
        raise UnsatisfiableError(core_pkgs)
