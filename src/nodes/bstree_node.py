from typing import Any, Optional
from .base_node import BaseNode


class BSTreeNode(BaseNode):

    def __init__(self,
                 value: Any,
                 left: Optional["BSTreeNode"] = None,
                 right: Optional["BSTreeNode"] = None,
                 parent: Optional["BSTreeNode"] = None) -> None:
        super().__init__(value)
        self._left = left
        self._right = right
        self._parent = parent

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def parent(self):
        return self._parent

    @property
    def is_leaf(self):
        return self.left is None and self.right is None

    @left.setter
    def left(self, new_left: "BSTreeNode"):
        self._left = new_left

    @right.setter
    def right(self, new_right: "BSTreeNode"):
        self._right = new_right

    @parent.setter
    def parent(self, new_parent: "BSTreeNode"):
        self._parent = new_parent

    @left.deleter
    def left(self):
        self._left = None

    @right.deleter
    def right(self):
        self._right = None

    @parent.deleter
    def parent(self):
        self._parent = None

    def preorder(self) -> str:
        """Preorder traversal: Visit root, then left, then right."""
        parts = [str(self.value)]
        if self.left:
            parts.append(self.left.preorder())
        if self.right:
            parts.append(self.right.preorder())
        return " ".join(parts)


    def inorder(self) -> str:
        """Inorder traversal: Visit left, then root, then right."""
        if self.left:
            parts.append(self.left.preorder())
        parts = [str(self.value)]
        if self.right:
            parts.append(self.right.preorder())
        return " ".join(parts)

    def postorder(self) -> str:
        """Postorder traversal: Visit left, then right, then root."""
        if self.left:
            parts.append(self.left.preorder())
        if self.right:
            parts.append(self.right.preorder())
        parts = [str(self.value)]
        return " ".join(parts)

    def __str__(self) -> str:
        return f"BSTNode({self.value})"

    def __repr__(self) -> str:
        return f"BSTNode({self.value}, left={repr(self.left)}, right={repr(self.right)})"
