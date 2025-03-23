def test_balance_factor_calculation(empty_avl):
    """Test that balance factors are calculated correctly"""
    # Create a simple tree
    empty_avl.insert(5)
    empty_avl.insert(3)
    empty_avl.insert(7)
    
    # Get balance factors (assuming you have a method to do this)
    def get_balance_factor(node):
        if node is None:
            return 0
        left_height = -1 if node.left is None else node.left.height
        right_height = -1 if node.right is None else node.right.height
        return left_height - right_height
    
    # Root should have balance factor 0
    assert get_balance_factor(empty_avl.root) == 0
    
    # Add another node to make left subtree deeper
    empty_avl.insert(2)
    
    # Root should now have balance factor 1
    assert get_balance_factor(empty_avl.root) == 1

def test_worst_case_insertion_left(empty_avl):
    """Test tree remains balanced with worst-case left insertion pattern"""
    # Insert in descending order (creates left-heavy insertions)
    values = list(range(20, 0, -1))
    for value in values:
        empty_avl.insert(value)
    
    # Check max height - should be logarithmic
    def get_height(node):
        if node is None:
            return -1
        return node.height
    
    # For 20 nodes, height should be around log2(20) ≈ 4.3, so max 5
    assert get_height(empty_avl.root) <= 5
    
    # Verify balance property holds for all nodes
    def verify_balance(node):
        if node is None:
            return True
        
        left_height = -1 if node.left is None else node.left.height
        right_height = -1 if node.right is None else node.right.height
        
        if abs(left_height - right_height) > 1:
            return False
        
        return verify_balance(node.left) and verify_balance(node.right)
    
    assert verify_balance(empty_avl.root)

def test_worst_case_insertion_right(empty_avl):
    """Test tree remains balanced with worst-case right insertion pattern"""
    # Insert in ascending order (creates right-heavy insertions)
    values = list(range(1, 21))
    for value in values:
        empty_avl.insert(value)
    
    # Check max height - should be logarithmic
    def get_height(node):
        if node is None:
            return -1
        return node.height
    
    # For 20 nodes, height should be around log2(20) ≈ 4.3, so max 5
    assert get_height(empty_avl.root) <= 5
    
    # Verify balance property holds for all nodes
    def verify_balance(node):
        if node is None:
            return True
        
        left_height = -1 if node.left is None else node.left.height
        right_height = -1 if node.right is None else node.right.height
        
        if abs(left_height - right_height) > 1:
            return False
        
        return verify_balance(node.left) and verify_balance(node.right)
    
    assert verify_balance(empty_avl.root)

def test_alternating_insertions(empty_avl):
    """Test tree remains balanced with alternating insertion pattern"""
    # Insert in a pattern that alternates between causing left and right rotations
    values = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93]
    for value in values:
        empty_avl.insert(value)
    
    # Verify all nodes have correct heights
    def verify_heights(node):
        if node is None:
            return True
        
        left_height = -1 if node.left is None else node.left.height
        right_height = -1 if node.right is None else node.right.height
        
        expected_height = 1 + max(left_height, right_height)
        if node.height != expected_height:
            return False
        
        return verify_heights(node.left) and verify_heights(node.right)
    
    assert verify_heights(empty_avl.root)
    
    # Verify tree is balanced
    def verify_balance(node):
        if node is None:
            return True
        
        left_height = -1 if node.left is None else node.left.height
        right_height = -1 if node.right is None else node.right.height
        
        if abs(left_height - right_height) > 1:
            return False
        
        return verify_balance(node.left) and verify_balance(node.right)
    
    assert verify_balance(empty_avl.root)

def test_mixed_operations(empty_avl):
    """Test tree remains balanced with mixed insertions and deletions"""
    # Insert some values
    for value in [10, 5, 15, 3, 7, 12, 17]:
        empty_avl.insert(value)
    
    # Delete some values
    empty_avl.delete(3)
    empty_avl.delete(12)
    
    # Insert more values
    empty_avl.insert(4)
    empty_avl.insert(11)
    
    # Delete and insert more
    empty_avl.delete(7)
    empty_avl.insert(8)
    
    # Verify tree maintains AVL properties
    def verify_avl_property(node):
        if node is None:
            return True, -1
        
        is_left_avl, left_height = verify_avl_property(node.left)
        is_right_avl, right_height = verify_avl_property(node.right)
        
        if not (is_left_avl and is_right_avl):
            return False, 0
        
        # Check balance factor
        if abs(left_height - right_height) > 1:
            return False, 0
        
        # Check height correctness
        expected_height = 1 + max(left_height, right_height)
        if node.height != expected_height:
            return False, 0
        
        return True, expected_height
    
    is_avl, _ = verify_avl_property(empty_avl.root)
    assert is_avl
