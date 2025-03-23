def test_insert_root(empty_avl):
    """Test inserting first node (root)"""
    empty_avl.insert(5)
    assert empty_avl.root.value == 5
    assert empty_avl.root.height == 0
    assert empty_avl.root.left is None
    assert empty_avl.root.right is None

def test_insert_maintain_bst_property(empty_avl):
    """Test that AVL maintains BST property after insertion"""
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        empty_avl.insert(value)

    # Verify BST property (in-order traversal gives sorted values)
    result = []
    def in_order(node):
        if node:
            in_order(node.left)
            result.append(node.value)
            in_order(node.right)

    in_order(empty_avl.root)
    assert result == sorted(values)

def test_height_update_after_insertion(empty_avl):
    """Test that heights are correctly updated after insertion"""
    empty_avl.insert(5)  # root
    assert empty_avl.root.height == 0

    empty_avl.insert(3)  # left child
    assert empty_avl.root.height == 1
    assert empty_avl.root.left.height == 0

    empty_avl.insert(7)  # right child
    assert empty_avl.root.height == 1
    assert empty_avl.root.left.height == 0
    assert empty_avl.root.right.height == 0

def test_left_rotation(empty_avl):
    """Test left rotation during insertion (right-heavy case)"""
    # Create right-heavy tree
    empty_avl.insert(3)
    empty_avl.insert(5)
    empty_avl.insert(7)

    # After balancing, the tree should have 5 as root
    assert empty_avl.root.value == 5
    assert empty_avl.root.left.value == 3
    assert empty_avl.root.right.value == 7

    # Check heights are updated correctly
    assert empty_avl.root.height == 1
    assert empty_avl.root.left.height == 0
    assert empty_avl.root.right.height == 0

def test_right_rotation(empty_avl):
    """Test right rotation during insertion (left-heavy case)"""
    # Create left-heavy tree
    empty_avl.insert(7)
    empty_avl.insert(5)
    empty_avl.insert(3)

    # After balancing, the tree should have 5 as root
    assert empty_avl.root.value == 5
    assert empty_avl.root.left.value == 3
    assert empty_avl.root.right.value == 7

    # Check heights are updated correctly
    assert empty_avl.root.height == 1
    assert empty_avl.root.left.height == 0
    assert empty_avl.root.right.height == 0

def test_left_right_rotation(empty_avl):
    """Test left-right (double) rotation"""
    # Create left-right case
    empty_avl.insert(7)
    empty_avl.insert(3)
    empty_avl.insert(5)

    # After balancing, the tree should have 5 as root
    assert empty_avl.root.value == 5
    assert empty_avl.root.left.value == 3
    assert empty_avl.root.right.value == 7

def test_right_left_rotation(empty_avl):
    """Test right-left (double) rotation"""
    # Create right-left case
    empty_avl.insert(3)
    empty_avl.insert(7)
    empty_avl.insert(5)

    # After balancing, the tree should have 5 as root
    assert empty_avl.root.value == 5
    assert empty_avl.root.left.value == 3
    assert empty_avl.root.right.value == 7

def test_complex_insertion_sequence(empty_avl):
    """Test tree balance with a complex insertion sequence"""
    # Insert values that require multiple rotations
    values = [10, 5, 15, 3, 7, 12, 20, 2, 4, 6, 8, 11, 13, 18, 25]
    for value in values:
        empty_avl.insert(value)

    # Verify balance factor for each node
    def verify_balance_factor(node):
        if node is None:
            return True

        left_height = -1 if node.left is None else node.left.height
        right_height = -1 if node.right is None else node.right.height
        balance_factor = left_height - right_height

        # Balance factor must be between -1 and 1
        if abs(balance_factor) > 1:
            return False

        # Height must be 1 + max of children's heights
        expected_height = 1 + max(left_height, right_height)
        if node.height != expected_height:
            return False

        # Verify children recursively
        return verify_balance_factor(node.left) and verify_balance_factor(node.right)

    assert verify_balance_factor(empty_avl.root)
