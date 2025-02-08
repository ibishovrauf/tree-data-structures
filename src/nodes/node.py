from typing import Any, Dict
from functools import total_ordering


@total_ordering
class Node:
    def __init__(self, value: Any, childs: Dict[str, "Node"]) -> None:
        self._value = value
        self._childs = childs

    @property
    def value(self) -> Any:
        return self._value
    
    @property
    def children(self) -> Dict[str, "Node"]:
        """Returns a copy of the child nodes to prevent direct modification."""
        return self._childs.copy()

    def add_child(self, key: str, child: "Node") -> None:
        """Adds a child node with a given key."""
        if not isinstance(child, Node):
            raise TypeError(f"Expected 'Node' instance, got {type(child).__name__}")
        self._childs[key] = child

    def remove_child(self, key: str) -> None:
        """Removes a child node by its key, if it exists."""
        if key in self._childs:
            del self._childs[key]

    def get_child(self, key: str) -> "Node":
        """Returns the child node for a given key or raises KeyError if not found."""
        return self._childs[key]

    def __eq__(self, other) -> bool:
        if not isinstance(other, Node):
            return NotImplemented
        return int(self._value) == int(other.value)

    def __lt__(self, other) -> bool:
        if not isinstance(other, Node):
            return NotImplemented
        try:
            return int(self._value) < int(other.value)
        except (ValueError, TypeError):
            raise TypeError("Node values must be comparable as integers.")

    def __str__(self) -> str:
        return f"Node({self._value}) with {len(self._childs)} children"

    def __repr__(self) -> str:
        childs_str = ", ".join(f"{key}: {value}" for key, value in self._childs.items())
        return f"Node(value={self._value}, childs={childs_str})"
