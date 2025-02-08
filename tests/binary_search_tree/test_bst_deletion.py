def test_delete_leaf(populated_bst):
    """Test deleting a leaf node"""
    populated_bst.delete(2)
    assert populated_bst.root.left.left is None

def test_delete_with_one_child(populated_bst):
    """Test deleting node with one child"""
    populated_bst.delete(3)
    assert populated_bst.root.left.value == 4
    assert populated_bst.root.left.left.value == 2


def test_delete_with_one_child(populated_bst_2):
    """Test deleting node with one child"""
    populated_bst_2.delete(10)
    assert populated_bst_2.search(9).right.value == 11
    assert populated_bst_2.search(12).left == None
