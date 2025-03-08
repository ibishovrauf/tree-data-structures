import copy
from src.nodes import AVLNode
from . import BinarySearchTree


class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()
    
    def insert(self, value: AVLNode | int) -> None:
        if not isinstance(value, AVLNode):
            value: AVLNode = AVLNode(value)
        super().insert(value)
        # self._update_and_rebalance_path(value)
    
    def _update_and_rebalance_path(self, node: AVLNode) -> None:        
        curr_node = node

        while curr_node:
            self._update_heights(curr_node)

            self._rebalance_node(curr_node)

            curr_node = curr_node.parent

    def _update_heights(self, node: AVLNode | int) -> None:
        if node.is_leaf:
            node.height = 0
            return

        childs = []
        if node.left:
            childs.append(node.left)
        
        if node.right:
            childs.append(node.right)

        new_height = max(childs, key=lambda x: x.height).height + 1
        node.height = new_height

    def _rebalance_node(self, node: AVLNode | int) -> None:
        if node.is_leaf:
            return
        
        left_node = node.left
        right_node = node.right
        
        left_height = left_node.height if isinstance(left_node, AVLNode) else -1
        right_height = right_node.height if isinstance(right_node, AVLNode) else -1

        if (left_height - right_height) >= 1:
            self._left_rotate(node)

        elif (left_height - right_height) <= -1:
            # self._right_rotate()
            pass

    def _left_rotate(self, node: AVLNode | int) -> None:
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


if __name__ == "__main__":
    tree = AVLTree()
    tree.insert(1)
    tree.insert(0)
    tree.insert(3)
    tree.insert(2)
    tree.insert(10)
    print(tree.root.height)