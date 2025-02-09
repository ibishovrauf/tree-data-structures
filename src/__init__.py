from .nodes import BSTreeNode, TrieNode, BTreeNode, RedBlackNode
from .trees import BinarySearchTree, Trie, RedBlackTree
from .visualization import visualization_worker

# Version information
__version__ = '1.0.0'

# Package metadata
__author__ = 'Rauf Ibishov'
__email__ = 'ibisovrauf183@gmail.com'

# All symbols that should be exported when using "from src import *"
__all__ = [
    'BSTreeNode',
    'TrieNode',
    'BTreeNode',
    'RedBlackNode',
    'BinarySearchTree',
    'Trie',
    'RedBlackTree',
]

# Optional: Package-level configuration
DEFAULT_TREE_TYPE = BinarySearchTree

# Optional: Package initialization code
def initialize_logging():
    """Set up logging for the package"""
    import logging
    logging.basicConfig(level=logging.INFO)

# Optional: Factory functions
def create_tree(tree_type=DEFAULT_TREE_TYPE):
    """Factory function to create new tree instances"""
    return tree_type()
