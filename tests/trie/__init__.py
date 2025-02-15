from .test_trie_base import (
    test_init,
    test_insert_empty_string,
    test_insert_multiple_words,
    test_insert_single_word,
)
from .test_trie_deletion import (
    test_delete_empty_string,
    test_delete_existing_word,
    test_delete_existing_word_v2,
    test_delete_prefix_word,
)
from .test_trie_edge_cases import (
    test_insert_case_sensitivity,
    test_special_characters,
)
from .test_trie_search import (
    test_search_empty_string,
    test_search_existing_word,
)
from .test_true_startwith import (
    test_starts_with_empty_string,
    test_starts_with_existing_prefix,
    test_starts_with_nonexistent_prefix,
)

__all__ = [
    "test_init",
    "test_insert_empty_string",
    "test_insert_multiple_words",
    "test_insert_single_word",
    "test_delete_empty_string",
    "test_delete_existing_word",
    "test_delete_existing_word_v2",
    "test_delete_prefix_word",
    "test_insert_case_sensitivity",
    "test_special_characters",
    "test_search_empty_string",
    "test_search_existing_word",
    "test_starts_with_empty_string",
    "test_starts_with_existing_prefix",
    "test_starts_with_nonexistent_prefix",
]

if __name__ == "__main__":
    import pytest
    pytest.main()
