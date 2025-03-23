import pytest

from src.nodes.avl_node import AVLNode


def test_init(empty_avl):
    """Test initialization of empty AVL tree"""
    assert empty_avl.root is None

def test_node_height_property():
    """Test AVLNode height property getter and setter"""
    node = AVLNode(10)
    assert node.height == 0
    
    node.height = 2
    assert node.height == 2
    
    # Test height validation
    with pytest.raises(ValueError):
        node.height = "invalid"

def test_create_node_override(empty_avl):
    """Test that _create_node creates AVLNode instances"""
    empty_avl.insert(5)
    assert isinstance(empty_avl.root, AVLNode)
    assert empty_avl.root.height == 0
