from src import BSTreeNode


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

    # Check root
    assert empty_bst.root.value == 5

    # Check left subtree
    assert empty_bst.root.left.value == 3
    assert empty_bst.root.left.left.value == 2
    assert empty_bst.root.left.right.value == 4

    # Check right subtree
    assert empty_bst.root.right.value == 7
    assert empty_bst.root.right.left.value == 6
    assert empty_bst.root.right.right.value == 8


def test_insert_duplicate(empty_bst):
    """Test inserting duplicate values"""
    empty_bst.insert(5)
    empty_bst.insert(5)
    assert empty_bst.root.left == None
    assert empty_bst.root.right == None


def test_insert_node_object(empty_bst):
    """Test inserting BSTreeNode objects directly"""
    node = BSTreeNode(5)
    empty_bst.insert(node)
    assert empty_bst.root is node
