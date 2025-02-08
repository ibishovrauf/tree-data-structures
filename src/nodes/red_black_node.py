from typing import Any, Literal, Optional
from .bstree_node import BSTreeNode


class RedBlackNode(BSTreeNode):
    def __init__(self, value: Any, color: Literal["red", "black"], parent: BSTreeNode, left: Optional[BSTreeNode] = None, right: Optional[BSTreeNode] = None) -> None:
        super().__init__(value, left, right)
        self.color = color
        self.parent = parent

    def __str__(self) -> str:
        left_val = self.left.value if self.left else None
        right_val = self.right.value if self.right else None
        return f"RedBlackNode({self._value}, color={self.color}, left={left_val}, right={right_val})"

    def __repr__(self) -> str:
        return f"BSTNode({self.value}, color={self.color}, left={self.left}, right={self.right})"
