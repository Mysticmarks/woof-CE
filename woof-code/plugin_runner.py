"""Dynamic loader for build plugins."""
from __future__ import annotations

import importlib
import json
import os
import sys
from typing import Any, Dict, List

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)


def load_manifest(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    return data.get("plugins", [])


def load_plugin(path: str):
    module_name, class_name = path.rsplit(".", 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)


def main(argv: List[str]) -> None:
    start = 0
    release = False
    for arg in list(argv):
        if arg.isdigit():
            start = int(arg)
            argv.remove(arg)
    if any(a in ("-release", "release") for a in argv):
        release = True
    manifest_path = os.path.join(BASE_DIR, "plugin_manifest.json")
    plugin_paths = load_manifest(manifest_path)[start:]
    context: Dict[str, Any] = {"cwd": BASE_DIR, "release": release}
    for plugin_path in plugin_paths:
        plugin_cls = load_plugin(plugin_path)
        plugin = plugin_cls()
        meta = plugin.metadata
        print(f"=== Running {meta.name} ({meta.description}) ===")
        plugin.init(context)
        plugin.run(context)
        plugin.teardown(context)


if __name__ == "__main__":
    main(sys.argv[1:])
