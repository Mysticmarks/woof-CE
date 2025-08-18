"""1download stage plugin."""
from __future__ import annotations

import subprocess
from typing import Any, Dict

from .interface import Plugin, PluginMetadata


class DownloadPlugin(Plugin):
    metadata = PluginMetadata(name="1download", description="Download required packages")

    def run(self, context: Dict[str, Any]) -> None:
        cwd = context["cwd"]
        subprocess.check_call(["./xlog", "1download"], cwd=cwd)
