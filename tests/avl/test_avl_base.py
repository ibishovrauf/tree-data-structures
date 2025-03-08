def test_init(empty_avl_tree):
    """Test initialization of empty AVLTree"""
    assert empty_avl_tree.root is None


def test_left_rotation(populated_avl_tree):
    populated_avl_tree._left_rotate(populated_avl_tree.root)
    assert populated_avl_tree.root.value == 3
    assert populated_avl_tree.root.left.value == 1
    assert populated_avl_tree.root.right.value == 4
    assert populated_avl_tree.root.left.right.value == 2


def test_left_rotation(populated_avl_tree_2):
    populated_avl_tree_2._left_rotate(populated_avl_tree_2.root)
    assert populated_avl_tree_2.root.value == 3
    assert populated_avl_tree_2.root.left.value == 1
    assert populated_avl_tree_2.root.right.value == 4