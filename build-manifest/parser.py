#!/usr/bin/env python3
"""Parse build manifest YAML into a DAG of callable build stages."""
from __future__ import annotations

import sys
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Callable, Dict, List

import yaml


@dataclass
class Stage:
    name: str
    run: str
    deps: List[str] = field(default_factory=list)
    artifacts: List[Dict[str, str]] = field(default_factory=list)


def load_manifest(path: str) -> Dict[str, Stage]:
    with open(path, "r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    stages: Dict[str, Stage] = {}
    for entry in data.get("stages", []):
        stage = Stage(
            name=entry["name"],
            run=entry["run"],
            deps=entry.get("deps", []),
            artifacts=entry.get("artifacts", []),
        )
        stages[stage.name] = stage
    return stages


def topological_order(stages: Dict[str, Stage]) -> List[str]:
    indegree = {name: 0 for name in stages}
    for stage in stages.values():
        for dep in stage.deps:
            indegree[stage.name] += 1
    queue: deque[str] = deque(name for name, deg in indegree.items() if deg == 0)
    order: List[str] = []
    graph: Dict[str, List[str]] = defaultdict(list)
    for stage in stages.values():
        for dep in stage.deps:
            graph[dep].append(stage.name)
    while queue:
        node = queue.popleft()
        order.append(node)
        for nbr in graph[node]:
            indegree[nbr] -= 1
            if indegree[nbr] == 0:
                queue.append(nbr)
    if len(order) != len(stages):
        raise ValueError("Cycle detected in manifest")
    return order


def build_functions(stages: Dict[str, Stage]) -> Dict[str, Callable[[], None]]:
    order = topological_order(stages)
    funcs: Dict[str, Callable[[], None]] = {}
    for name in order:
        stage = stages[name]

        def _make(stage: Stage = stage) -> Callable[[], None]:
            def run() -> None:
                print(f"Running {stage.name}: {stage.run}")
            return run

        funcs[name] = _make()
    return funcs


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} MANIFEST", file=sys.stderr)
        sys.exit(1)
    stages = load_manifest(sys.argv[1])
    order = topological_order(stages)
    funcs = build_functions(stages)
    print(f"Build order: {order}")
    for name in order:
        funcs[name]()


if __name__ == "__main__":
    main()
