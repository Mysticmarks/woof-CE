"""0setup stage plugin."""
from __future__ import annotations

import subprocess
from typing import Any, Dict

from .interface import Plugin, PluginMetadata


class SetupPlugin(Plugin):
    metadata = PluginMetadata(name="0setup", description="Initial setup stage")

    def run(self, context: Dict[str, Any]) -> None:
        cwd = context["cwd"]
        subprocess.check_call(["./xlog", "0setup", "a"], cwd=cwd)
