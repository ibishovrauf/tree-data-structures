"""
This module implements a simple tree data structure using the Node class.

The Node class encapsulates a value and a collection of child nodes, allowing for the creation
of hierarchical structures. Each node stores its value and maintains a dictionary of its child
nodes, which can be accessed via a property that returns a copy to prevent direct modification.
The class provides methods to add, remove, and retrieve child nodes, and supports comparison
operations based on the integer conversion of node values (assuming the values can be converted
to integers).

Key Features:
    - Encapsulation of a value and a dictionary of child nodes.
    - Read-only properties for node value and children.
    - Methods to add, remove, and access child nodes.
    - Comparison operators (__eq__ and __lt__) for node instances.
    - Informative string representations (__str__ and __repr__) for easy debugging and display.

Usage Example:
    >>> root = Node(1)
    >>> child = Node(2)
    >>> root.add_child("child1", child)
    >>> print(root)
    Node(1) with 1 children
"""
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


if __name__ == "__main__":
    left_child = Node(1, {})
    left_child = Node(3, {"left": left_child})
    right_child = Node(7, {})
    parent = Node(5, {"left": left_child, "right": right_child})

    print(str(parent))   # Output: Node(5) with children {'left': 3, 'right': 7}
    print(repr(parent))  # Output: Node(value=5, childs={'left': 3, 'right': 7})
    parent.get_children()