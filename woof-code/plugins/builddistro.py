"""3builddistro stage plugin."""
from __future__ import annotations

import subprocess
from typing import Any, Dict

from .interface import Plugin, PluginMetadata


class BuildDistroPlugin(Plugin):
    metadata = PluginMetadata(name="3builddistro", description="Assemble final distribution")

    def run(self, context: Dict[str, Any]) -> None:
        cwd = context["cwd"]
        cmd = ["./xlog", "3builddistro"]
        if context.get("release"):
            cmd.append("-release")
        subprocess.check_call(cmd, cwd=cwd)
