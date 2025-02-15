def test_is_leaf_empty(empty_bst):
    """Test is_leaf on empty tree"""
    assert empty_bst.root is None


def test_is_leaf_single_node(empty_bst):
    """Test is_leaf on tree with single node"""
    empty_bst.insert(5)
    assert empty_bst.root.is_leaf


def test_is_leaf_with_children(populated_bst):
    """Test is_leaf on nodes with children"""
    assert not populated_bst.root.is_leaf
    assert populated_bst.root.left.left.is_leaf
