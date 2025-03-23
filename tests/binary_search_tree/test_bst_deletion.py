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

def test_delete_all_nodes(populated_bst):
    """Test deleting all nodes from the tree"""
    values = []
    def collect_values(node):
        if node:
            collect_values(node.left)
            values.append(node.value)
            collect_values(node.right)
    
    collect_values(populated_bst.root)
    
    # Delete all values
    for value in values[::-1]:
        print(f"{value} deleted")
        populated_bst.delete(value)
    # Tree should be empty
    assert populated_bst.root is None
