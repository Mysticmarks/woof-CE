"""Plugin interface for woof build stages."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class PluginMetadata:
    """Descriptive information about a plugin."""

    name: str
    description: str = ""
    version: str = "1.0"


class Plugin:
    """Base class for build plugins."""

    metadata: PluginMetadata

    def __init__(self) -> None:
        if not hasattr(self, "metadata"):
            raise ValueError("Plugin subclass must define metadata")

    def init(self, context: Dict[str, Any]) -> None:  # noqa: D401
        """Prepare plugin state."""

    def run(self, context: Dict[str, Any]) -> None:  # noqa: D401
        """Execute plugin action."""

    def teardown(self, context: Dict[str, Any]) -> None:  # noqa: D401
        """Clean up plugin state."""
