from src import BSTreeNode


def test_search_empty(empty_bst):
    """Test searching in empty tree"""
    result = empty_bst.search(5)
    assert result is None

def test_search_existing(populated_bst):
    """Test searching for existing values"""
    result = populated_bst.search(4)
    assert result is not None
    assert result.value == 4

def test_search_missing(populated_bst):
    """Test searching for non-existent values"""
    populated_bst.insert(5)
    result = populated_bst.search(10)
    assert result is None

def test_search_node_object(populated_bst):
    """Test searching with BSTreeNode objects"""
    populated_bst.insert(5)
    search_node = BSTreeNode(5)
    result = populated_bst.search(search_node)
    assert result is not None
    assert result.value == 5

def test_contains(populated_bst):
    """Test __contains__ method"""
    assert ( 5 in populated_bst) == True
    assert ( 3 in populated_bst) == True
    assert ( 7 in populated_bst) == True
    assert (10 in populated_bst) == False
