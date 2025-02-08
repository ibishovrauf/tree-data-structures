def test_init(empty_bst):
    """Test initialization of empty BST"""
    assert empty_bst.root is None

def test_insert_root(empty_bst):
    """Test inserting first node (root)"""
    empty_bst.insert(5)
    assert empty_bst.root.value == 5
    assert empty_bst.root.left is None
    assert empty_bst.root.right is None

def test_insert_multiple(empty_bst):
    """Test inserting multiple values in correct positions"""
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        empty_bst.insert(value)
    
    assert empty_bst.root.value == 5
    assert empty_bst.root.left.value == 3
    assert empty_bst.root.right.value == 7
