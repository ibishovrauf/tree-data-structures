from typing import Any, Dict, Optional
from copy import deepcopy

from src.nodes.base_node import BaseNode


class TrieNode(BaseNode):

    def __init__(
                self,
                value: Any,
                children: Dict[str, "TrieNode"] = dict()
            ) -> None:
        super().__init__(value)
        self._children = deepcopy(children)
        self._wordEnd = False

    @property
    def children(self) -> Dict[str, "TrieNode"]:
        return self._children

    @children.setter
    def children(self, value: Dict[str, "TrieNode"]) -> None:
        """Set the child nodes after validating the input dictionary."""
        if not isinstance(value, dict):
            raise TypeError("children must be a dictionary.")
        for key, node in value.items():
            if not isinstance(key, str):
                raise TypeError("All keys in children must be strings.")
            if not isinstance(node, TrieNode):
                raise TypeError(
                    "All values in children must be TrieNode instances.")
        self._children = value

    @property
    def wordEnd(self):
        return self._wordEnd

    @wordEnd.setter
    def wordEnd(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("wordEnd must be a boolean")
        self._wordEnd = value

    @property
    def child_count(self) -> int:
        return len(self._children.keys())

    def add_child(self, value: Dict[str, "TrieNode"]) -> None:
        if not isinstance(value, dict):
            raise TypeError("children must be a dictionary.")

        for key, node in value.items():
            if not isinstance(key, str):
                raise TypeError("All keys in children must be strings.")

            if not isinstance(node, TrieNode):
                raise TypeError(
                    "All values in children must be TrieNode instances.")

            self._children[key] = node

    def __str__(self) -> str:
        children_str = ", ".join(key for key in self._children.keys())
        return f"Node({self.value}) with {len(self.children)} children: {children_str}"

    def __repr__(self) -> str:
        children_str = ", ".join(f"{key}: {value}"
                               for key, value in self._children.items())
        return f"Node(value={self._value}, children={children_str})"
