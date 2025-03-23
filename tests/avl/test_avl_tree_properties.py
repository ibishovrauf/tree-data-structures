def test_height_property_after_rotations(empty_avl):
    """Test that height property is maintained after rotations"""
    # Create a tree that requires left rotation
    empty_avl.insert(5)
    empty_avl.insert(10)
    empty_avl.insert(15)  # Should trigger rotation
    
    # After rotation, root should be 10
    assert empty_avl.root.value == 10
    
    # Verify heights
    assert empty_avl.root.height == 1
    assert empty_avl.root.left.height == 0
    assert empty_avl.root.right.height == 0

def test_get_min_max_values(balanced_avl):
    """Test getting minimum and maximum values"""
    # Implement min/max value retrieval methods if not available
    def get_min_value(node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value
    
    def get_max_value(node):
        current = node
        while current.right is not None:
            current = current.right
        return current.value
    
    # Test min/max
    assert get_min_value(balanced_avl.root) == 3
    assert get_max_value(balanced_avl.root) == 17

def test_inorder_traversal(balanced_avl):
    """Test that in-order traversal gives sorted values"""
    values = []
    
    def inorder(node):
        if node:
            inorder(node.left)
            values.append(node.value)
            inorder(node.right)
    
    inorder(balanced_avl.root)
    assert values == [3, 5, 7, 10, 12, 15, 17]

def test_height_calculation(balanced_avl):
    """Test that height is calculated correctly"""
    # Verify specific node heights
    assert balanced_avl.root.height == 2  # Root is at height 2
    
    # Left subtree heights
    assert balanced_avl.root.left.height == 1
    assert balanced_avl.root.left.left.height == 0
    assert balanced_avl.root.left.right.height == 0
    
    # Right subtree heights
    assert balanced_avl.root.right.height == 1
    assert balanced_avl.root.right.left.height == 0
    assert balanced_avl.root.right.right.height == 0

def test_size_calculation(balanced_avl):
    """Test calculating the size (number of nodes) in the tree"""
    def count_nodes(node):
        if node is None:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)
    
    assert count_nodes(balanced_avl.root) == 7

def test_is_balanced_property(balanced_avl):
    """Test that the tree maintains the AVL balance property"""
    def is_avl_balanced(node):
        if node is None:
            return True, -1
        
        is_left_balanced, left_height = is_avl_balanced(node.left)
        is_right_balanced, right_height = is_avl_balanced(node.right)
        
        if not (is_left_balanced and is_right_balanced):
            return False, 0
        
        if abs(left_height - right_height) > 1:
            return False, 0
        
        return True, 1 + max(left_height, right_height)
    
    