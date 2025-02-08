from typing import Any, Dict, Optional
from .base_node import BaseNode

class TrieNode(BaseNode):
    def __init__(self, value: Any, childs: Optional[Dict[str, "TrieNode"]] = {}) -> None:
        super().__init__(value)
        self._childs = childs

    @property
    def childs(self):
        return self._childs.copy()

    def __str__(self) -> str:
        return f"Node({self.value}) with {len(self.childs)} children"

    def __repr__(self) -> str:
        childs_str = ", ".join(f"{key}: {value}" for key, value in self._childs.items())
        return f"Node(value={self._value}, childs={childs_str})"
