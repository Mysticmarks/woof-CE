"""2createpackages stage plugin."""
from __future__ import annotations

import subprocess
from typing import Any, Dict

from .interface import Plugin, PluginMetadata


class CreatePackagesPlugin(Plugin):
    metadata = PluginMetadata(name="2createpackages", description="Create package layer")

    def run(self, context: Dict[str, Any]) -> None:
        cwd = context["cwd"]
        subprocess.check_call(["./xlog", "2createpackages", "-all"], cwd=cwd)
