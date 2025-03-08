from typing import Any
from . import BSTreeNode


class AVLNode(BSTreeNode):
    def __init__(self, value: Any, left: BSTreeNode | None = None, right: BSTreeNode | None = None) -> None:
        super().__init__(value, left, right)
        self._height : int = 0

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height: int):
        if not isinstance(new_height, int):
            raise ValueError("The height must be integer")
        self._height = new_height
