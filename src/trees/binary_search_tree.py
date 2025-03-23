from copy import deepcopy
import threading
from typing import Any, Optional
from src.nodes import BSTreeNode


class BinarySearchTree:

    def __init__(self):
        self._root: Optional[BSTreeNode] = None
        self._lock = threading.Lock()
    
    def insert(self, value: BSTreeNode | int) -> None:
        if not isinstance(value, BSTreeNode):
            value: BSTreeNode = BSTreeNode(value)

        if not self.root:
            if self._lock:
                self._root = value
            return

        current_node = self.root
        while True:
            if current_node < value:
                if current_node.right is None:
                    if self._lock:
                        current_node.right = value
                        value.parent = current_node
                    break
                current_node = current_node.right
            elif current_node > value:
                if current_node.left is None:
                    if self._lock:
                        current_node.left = value
                        value.parent = current_node
                    break
                current_node = current_node.left
            else:
                print(f"The value {value} already exsists in Tree")
                break

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
            if not current_node.parent:
                self.root = None
                return
            elif current_node.parent.left == value:
                del current_node.parent.left
                return
            del current_node.parent.right
        elif current_node.right:
            curr = current_node.right

            if curr.is_leaf:
                current_node.value = curr.value
                del current_node.right
                return

            while curr.left:
                curr = curr.left
            current_node.value = curr.value
            if not curr.is_leaf:
                curr.parent.right = curr.right
            else:
                curr.parent.left = None
        else:
            curr = current_node.left

            if curr.is_leaf:
                current_node.value = curr.value
                del current_node.left
                return
            while curr.right:
                curr = curr.right
            current_node.value = curr.value
            if not curr.is_leaf:
                curr.parent.left = curr.left
            else:
                curr.parent.right = None

    @property
    def root(self) -> Optional[BSTreeNode]:
        return self._root

    @root.setter
    def root(self, node) -> None:
        self._root = node

    def __contains__(self, value):
        return self.search(value=value) != None

    def __str__(self) -> str:
        return str(self.root)

    def __repr__(self) -> str:
        return repr(self.root)

    def get_snapshot(self) -> Optional[BSTreeNode]:
        """
        Return a deep copy of the current tree root.
        """
        with self._lock:
            return deepcopy(self.root)
