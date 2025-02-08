from typing import Any, Optional
from .base_node import BaseNode


class BSTreeNode(BaseNode):
    def __init__(self, value: Any, left: Optional["BSTreeNode"] = None, right: Optional["BSTreeNode"] = None) -> None:
        super().__init__(value)
        self._left = left
        self._right = right

    @property
    def left(self):
        return self._left
    
    @property
    def right(self):
        return self._right
    
    @property
    def is_leaf(self):
        return self.left is None and self.right is None

    @left.setter
    def left(self, new_left: "BSTreeNode"):
        if not isinstance(new_left, BSTreeNode):
            raise ValueError("The leaf node must be BSTreeNode class")
        self._left = new_left

    @right.setter
    def right(self, new_right: "BSTreeNode"):
        if not isinstance(new_right, BSTreeNode):
            raise ValueError("The leaf node must be BSTreeNode class")
        self._right = new_right

    @left.deleter
    def left(self):
        self._left = None

    @right.deleter
    def right(self):
        self._right = None

    def __str__(self) -> str:
        left_val = self.left.value if self.left else None
        right_val = self.right.value if self.right else None
        return f"BSTNode({self.value}, left={left_val}, right={right_val})"

    def __repr__(self) -> str:
        return f"BSTNode({self.value}, left={self.left}, right={self.right})"
    