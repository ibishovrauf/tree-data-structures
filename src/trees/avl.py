from typing import Optional
from src.nodes import AVLNode
from . import BinarySearchTree


class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()
    
    def insert(self, value: AVLNode | int) -> None:
        if not isinstance(value, AVLNode):
            value: AVLNode = AVLNode(value)
        super().insert(value)
        self._update_heights()
        self._rebalance_upwards(value)
    
    def delete(self, value: AVLNode | int):
        if not isinstance(value, AVLNode):
            value: AVLNode = AVLNode(value)

        node = self.search(value)
        starting_node = node.parent if node else None
        super().delete(value)
        if not starting_node:
            starting_node = self.root

        self._update_heights()
        self._rebalance_upwards(starting_node)

    def _rebalance_upwards(self, node: AVLNode) -> None:        
        curr_node = node

        while curr_node:
            self._rebalance_node(curr_node)
            curr_node = curr_node.parent

    def _update_heights(self) -> None:
        if not self.root:
            return
        elif self.root.is_leaf:
            self.root.height = 0
            return
        self.root.height = max(self._calculate_height(self.root.left), self._calculate_height(self.root.right))+1

    def _calculate_height(self, node: Optional[AVLNode]) -> int:
        if not node:
            return -1
        node.height = max(self._calculate_height(node.left), self._calculate_height(node.right))+1
        return node.height

    def _rebalance_node(self, node: AVLNode) -> None:
        if node.is_leaf or node.height < 2:
            return
        
        left_node = node.left
        right_node = node.right
        
        left_height = left_node.height if isinstance(left_node, AVLNode) else -1
        right_height = right_node.height if isinstance(right_node, AVLNode) else -1

        if (left_height - right_height) < -1:
            if right_node:
                right_left_node = right_node.left
                right_right_node = right_node.right
                right_left_height = right_left_node.height if isinstance(right_left_node, AVLNode) else -1
                right_right_height = right_right_node.height if isinstance(right_right_node, AVLNode) else -1
                if (right_left_height - right_right_height) > 0:
                    self._right_rotate(right_node)
            self._left_rotate(node)

        elif (left_height - right_height) > 1:
            if left_node:
                left_left_node = left_node.left
                left_right_node = left_node.right
                left_left_height = left_left_node.height if isinstance(left_left_node, AVLNode) else -1
                left_right_height = left_right_node.height if isinstance(left_right_node, AVLNode) else -1
                if (left_left_height - left_right_height) < 0:
                    self._left_rotate(left_node)
            self._right_rotate(node)
        self._update_heights()

    def _left_rotate(self, node: AVLNode | int) -> None:
        print("Left")
        node_copy = AVLNode(node.value)
        if node.left:
            node_copy.left = node.left
            node.left.parent = node_copy
        
        node.value = node.right.value

        node.left = node_copy
        node_copy.parent = node

        node_copy.right = node.right.left
        if node.right.left:
            node.right.left.parent = node_copy
    
        if node.right.right:
            node.right.right.parent = node
        node.right = node.right.right

    def _right_rotate(self, node: AVLNode | int) -> None:
        print("RIght")
        node_copy = AVLNode(node.value)
        if node.right:
            node_copy.right = node.right
            node.right.parent = node_copy
        
        node.value = node.left.value

        node.right = node_copy
        node_copy.parent = node

        node_copy.left = node.left.right
        if node.left.right:
            node.left.right.parent = node_copy
    
        if node.left.left:
            node.left.left.parent = node
        node.left = node.left.left
