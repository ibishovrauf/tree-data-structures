from typing import Any
from .base_node import BaseNode


class BTreeNode(BaseNode):
    def __init__(self, value: Any, keys_per_node: int) -> None:
        super().__init__(value)
        self._keys_per_node = keys_per_node
        self._keys: list[Any] = []
        self._children: list['BTreeNode'] = []
        
    @property
    def keys(self) -> list[Any]:
        return self._keys
    
    @property
    def children(self) -> list['BTreeNode']:
        return self._children

    def __str__(self) -> str:
        return f"BTreeNode(keys={self.keys}, children_count={len(self.children)})"
    
    def __repr__(self) -> str:
        return f"BTreeNode(keys={self.keys}, children={self.children})"