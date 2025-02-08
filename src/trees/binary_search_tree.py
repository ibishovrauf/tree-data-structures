from typing import Any, Optional
from src.nodes import BSTreeNode


class BinarySearchTree:

    def __init__(self):
        self._root: Optional[BSTreeNode] = None

    def insert(self, value: BSTreeNode | int) -> None:
        if not isinstance(value, BSTreeNode):
            value: BSTreeNode = BSTreeNode(value)

        if not self.root:
            self._root = value
            return

        current_node = self.root
        while True:
            if current_node < value:
                if current_node.right is None:
                    current_node.right = value
                    break
                current_node = current_node.right
            else:
                if current_node.left is None:
                    current_node.left = value
                    break
                current_node = current_node.left

    def search(self, value: BSTreeNode | int) -> Optional[BSTreeNode]:
        if not isinstance(value, BSTreeNode):
            value: BSTreeNode = BSTreeNode(value)

        current_node = self.root
        while True:
            if not current_node:
                return None
            elif current_node == value:
                return current_node
            elif current_node < value:
                current_node = current_node.right
            else:
                current_node = current_node.left

    def delete(self, value: int) -> None:
        if not isinstance(value, BSTreeNode):
            value: BSTreeNode = BSTreeNode(value)
        current_node = self.root
        while True:
            if not current_node:
                return None
            elif current_node == value:

                break
            elif current_node < value:
                parent = current_node
                current_node = current_node.right
            else:
                parent = current_node
                current_node = current_node.left
        if current_node.is_leaf:
            if parent.left == value:
                del parent.left
                return
            del parent.right
        elif current_node.right:
            curr = current_node.right
            if curr.is_leaf:
                current_node.value = curr.value
                del current_node.right
                return
            while not curr.left.is_leaf:
                curr = curr.left
            current_node.value = curr.left.value
            del curr.left
        else:
            curr = current_node.left
            if curr.is_leaf:
                current_node.value = curr.value
                del current_node.left
                return
            while not curr.right.is_leaf:
                curr = curr.right
            current_node.value = curr.right.value
            del curr.right

    @property
    def root(self) -> Optional[BSTreeNode]:
        return self._root

    def __contains__(self, value):
        return self.search(value=value) != None

    def __str__(self) -> str:
        return str(self.root)

    def __repr__(self) -> str:
        return repr(self.root)
