def test_empty_tree_operations(empty_avl):
    """Test operations on an empty tree"""
    # Search in empty tree
    assert empty_avl.search(5) is None
    
    # Delete from empty tree shouldn't raise error
    empty_avl.delete(5)  # Should not raise exception
    assert empty_avl.root is None

def test_insert_duplicate_values(empty_avl):
    """Test inserting duplicate values"""
    empty_avl.insert(5)
    empty_avl.insert(5)  # Insert duplicate
    
    # Count occurrences of 5
    count = 0
    def count_value(node, value):
        nonlocal count
        if node is None:
            return
        if node.value == value:
            count += 1
        count_value(node.left, value)
        count_value(node.right, value)
    
    count_value(empty_avl.root, 5)
    
    # Behavior depends on implementation - either 1 (replace) or 2 (allow duplicates)
    # Check your implementation's expected behavior
    assert count in (1, 2)

def test_insert_large_number_of_nodes(empty_avl):
    """Test inserting a large number of nodes"""
    # Insert 1000 nodes
    import random
    values = list(range(1000))
    random.shuffle(values)
    
    for value in values:
        empty_avl.insert(value)
    
    # Height should be logarithmic
    def get_height(node):
        if node is None:
            return -1
        return node.height
    
    # For 1000 nodes, height should be around log2(1000) ≈ 10
    assert get_height(empty_avl.root) <= 15
    
    # Verify all values can be found
    for value in values:
        found = empty_avl.search(value)
        assert found is not None
        assert found.value == value

def test_insert_sorted_values(empty_avl):
    """Test inserting values in sorted order (stress test rotations)"""
    # Insert 100 values in ascending order
    for i in range(100):
        empty_avl.insert(i)
    
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

def test_delete_all_nodes_specific_order(empty_avl):
    """Test deleting all nodes in specific order"""
    # Insert nodes
    values = [10, 5, 15, 3, 7, 12, 17]
    for value in values:
        empty_avl.insert(value)
    
    # Delete in post-order (leaves first)
    delete_order = [3, 7, 5, 12, 17, 15, 10]
    for value in delete_order:
        empty_avl.delete(value)
        
        # After each deletion, verify tree is still valid
        if empty_avl.root is not None:
            def verify_tree(node):
                if node is None:
                    return True
                
                left_height = -1 if node.left is None else node.left.height
                right_height = -1 if node.right is None else node.right.height
                
                # Check balance factor
                if abs(left_height - right_height) > 1:
                    return False
                
                # Check height is correct
                expected_height = 1 + max(left_height, right_height)
                if node.height != expected_height:
                    return False
                
                return verify_tree(node.left) and verify_tree(node.right)
            
            assert verify_tree(empty_avl.root)
    
    # Tree should be empty
    assert empty_avl.root is None

def test_node_height_correctness_after_operations(empty_avl):
    """Test that node heights are correctly maintained after various operations"""
    # Perform a mix of insertions and deletions
    operations = [
        ('insert', 10), ('insert', 5), ('insert', 15), 
        ('insert', 3), ('insert', 7), ('delete', 3),
        ('insert', 12), ('delete', 7), ('insert', 17),
        ('delete', 15), ('insert', 8), ('delete', 10)
    ]
    
    for op, value in operations:
        if op == 'insert':
            empty_avl.insert(value)
        else:  # op == 'delete'
            empty_avl.delete(value)
        
        # After each operation, verify all heights are correct
        def verify_heights(node):
            if node is None:
                return True, -1
            
            is_left_heights_valid, left_height = verify_heights(node.left)
            is_right_heights_valid, right_height = verify_heights(node.right)
            
            if not (is_left_heights_valid and is_right_heights_valid):
                return False, 0
            
            expected_height = 1 + max(left_height, right_height)
            if node.height != expected_height:
                return False, 0
            
            return True, node.height
        
        if empty_avl.root is not None:
            is_heights_valid, _ = verify_heights(empty_avl.root)
            assert is_heights_valid

def test_one_node_tree(empty_avl):
    """Test operations on a tree with only one node"""
    # Insert single node
    empty_avl.insert(10)
    
    # Verify properties
    assert empty_avl.root.value == 10
    assert empty_avl.root.height == 0
    assert empty_avl.root.left is None
    assert empty_avl.root.right is None
    
    # Delete the node
    empty_avl.delete(10)
    assert empty_avl.root is None
    
    # Insert again and verify
    empty_avl.insert(20)
    assert empty_avl.root.value == 20
    assert empty_avl.root.height == 0
