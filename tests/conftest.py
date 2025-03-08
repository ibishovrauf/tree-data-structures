import pytest
from src import BinarySearchTree, Trie, AVLTree


@pytest.fixture
def empty_bst():
    return BinarySearchTree()


@pytest.fixture
def populated_bst():
    bst = BinarySearchTree()
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        bst.insert(value)
    return bst


@pytest.fixture
def populated_bst_2():
    bst = BinarySearchTree()
    values = [5, 3, 7, 2, 4, 6, 8, 1, 9, 0, 10, 12, 11, 13]
    for value in values:
        bst.insert(value)

    return bst


@pytest.fixture
def empty_trie():
    return Trie()


@pytest.fixture
def populated_trie():
    trie = Trie()
    words = ["cat", "cats", "catch", "dog", "dogs", "do"]
    for word in words:
        trie.insert(word)
    return trie


@pytest.fixture
def empty_avl_tree():
    return AVLTree()


@pytest.fixture
def populated_avl_tree():
    tree = AVLTree()
    values = [1, 3, 4, 2]
    for value in values:
        tree.insert(value)
    return tree


@pytest.fixture
def populated_avl_tree_2():
    tree = AVLTree()
    values = [1, 3, 4]
    for value in values:
        tree.insert(value)
    return tree


@pytest.fixture
def populated_avl_tree_3():
    tree = AVLTree()
    values = [4, 2, 1, 3]
    for value in values:
        tree.insert(value)
    return tree