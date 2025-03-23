def test_delete_leaf_node(balanced_avl):
    """Test deleting a leaf node"""
    balanced_avl.delete(3)
    
    # Verify node is deleted
    assert balanced_avl.search(3) is None
    assert balanced_avl.root.left.left is None
    
    # Verify tree is still balanced
    def is_balanced(node):
        if node is None:
            return True
        
        left_height = -1 if node.left is None else node.left.height
        right_height = -1 if node.right is None else node.right.height
        
        if abs(left_height - right_height) > 1:
            return False
        
        return is_balanced(node.left) and is_balanced(node.right)
    
    assert is_balanced(balanced_avl.root)

def test_delete_node_with_one_child(balanced_avl):
    """Test deleting a node with one child"""
    # First delete 3 to make 5 have only one child
    balanced_avl.delete(3)
    # Then delete 5
    balanced_avl.delete(5)
    
    # Verify 5 is replaced with 7
    assert balanced_avl.search(5) is None
    assert balanced_avl.root.left.value == 7
    
    # Verify tree is still balanced
    def verify_heights(node):
        if node is None:
            return True
        
        left_height = -1 if node.left is None else node.left.height
        right_height = -1 if node.right is None else node.right.height
        
        expected_height = 1 + max(left_height, right_height)
        if node.height != expected_height:
            return False
        
        return verify_heights(node.left) and verify_heights(node.right)
    
    assert verify_heights(balanced_avl.root)

def test_delete_node_with_two_children(balanced_avl):
    """Test deleting a node with two children"""
    # Delete 10 (root with two children)
    balanced_avl.delete(10)
    
    # Root should be replaced with predecessor or successor
    assert balanced_avl.root.value in (7, 12)  # Depending on implementation
    assert balanced_avl.search(10) is None
    
    # Verify tree is still balanced
    def is_balanced(node):
        if node is None:
            return True
        
        left_height = -1 if node.left is None else node.left.height
        right_height = -1 if node.right is None else node.right.height
        
        if abs(left_height - right_height) > 1:
            return False
        
        return is_balanced(node.left) and is_balanced(node.right)
    
    assert is_balanced(balanced_avl.root)

def test_delete_root_node(balanced_avl):
    """Test deleting the root node"""
    balanced_avl.delete(10)
    
    # Verify tree still maintains BST property
    def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
        if node is None:
            return True
        
        if node.value <= min_val or node.value >= max_val:
            return False
        
        return (is_bst(node.left, min_val, node.value) and 
                is_bst(node.right, node.value, max_val))
    
    assert is_bst(balanced_avl.root)

def test_delete_causing_rotation(empty_avl):
    """Test deletion that requires rotation to rebalance"""
    # Build a specific tree where deletion will cause imbalance
    values = [5, 3, 8, 2, 4, 7, 10, 1]
    for value in values:
        empty_avl.insert(value)
    
    # Delete 10, which should cause right subtree to be shorter
    empty_avl.delete(10)
    
    # Delete 1, which should cause left subtree to be shorter and trigger rotation
    empty_avl.delete(1)
    
    # Verify rotations occurred and tree is balanced
    def get_balance_factor(node):
        if node is None:
            return 0
        
        left_height = -1 if node.left is None else node.left.height
        right_height = -1 if node.right is None else node.right.height
        return left_height - right_height
    
    # Check every node's balance factor
    def check_balance_factors(node):
        if node is None:
            return True
        
        if abs(get_balance_factor(node)) > 1:
            return False
        
        return check_balance_factors(node.left) and check_balance_factors(node.right)
    
    assert check_balance_factors(empty_avl.root)

def test_delete_non_existent_value(balanced_avl):
    """Test deleting a value that doesn't exist in the tree"""
    # Store original structure
    original_root_value = balanced_avl.root.value
    
    # Try to delete non-existent value
    balanced_avl.delete(100)
    
    # Tree should remain unchanged
    assert balanced_avl.root.value == original_root_value
    
    # Verify tree structure is still valid
    def validate_tree(node):
        if node is None:
            return True
        
        # Check heights are correct
        left_height = -1 if node.left is None else node.left.height
        right_height = -1 if node.right is None else node.right.height
        
        expected_height = 1 + max(left_height, right_height)
        if node.height != expected_height:
            return False
        
        # Check balance factor
        if abs(left_height - right_height) > 1:
            return False
        
        return validate_tree(node.left) and validate_tree(node.right)
    
    assert validate_tree(balanced_avl.root)

def test_delete_all_nodes(balanced_avl):
    """Test deleting all nodes from the tree"""
    # Get all values in the tree
    values = []
    def collect_values(node):
        if node:
            collect_values(node.left)
            values.append(node.value)
            collect_values(node.right)
    
    collect_values(balanced_avl.root)
    
    # Delete all values
    for value in values:
        balanced_avl.delete(value)
    
    # Tree should be empty
    assert balanced_avl.root is None
