from .test_bst_base import (
    test_init,
    test_insert_multiple, 
    test_insert_root
)
from .test_bst_deletion import test_delete_leaf, test_delete_with_one_child
from .test_bst_insert import (
    test_insert_duplicate, 
    test_insert_multiple, 
    test_insert_node_object, 
    test_insert_root
)
from .test_bst_properties import (
    test_is_leaf_empty, 
    test_is_leaf_single_node, 
    test_is_leaf_with_children
)
from .test_bst_search import (
    test_contains, 
    test_search_empty, 
    test_search_existing, 
    test_search_missing,
    test_search_node_object
)

__all__ = [
    "test_init",
    "test_insert_multiple",
    "test_insert_root",
    "test_delete_leaf",
    "test_delete_with_one_child",
    "test_insert_duplicate",
    "test_insert_multiple",
    "test_insert_node_object",
    "test_insert_root",
    "test_is_leaf_empty",
    "test_is_leaf_single_node",
    "test_is_leaf_with_children",
    "test_contains",
    "test_search_empty",
    "test_search_existing",
    "test_search_missing",
    "test_search_node_object",
]

if __name__ == "__main__":
    import pytest
    pytest.main()