def test_insert_case_sensitivity(empty_trie):
    """Test case sensitivity in the trie"""
    empty_trie.insert("Cat")
    empty_trie.insert("cat")
    assert empty_trie.search("Cat") == True
    assert empty_trie.search("cat") == True
    assert empty_trie.search("CAT") == False


def test_special_characters(empty_trie):
    """Test handling of special characters"""
    test_words = ["hello!", "@world", "#python", "test-case"]
    for word in test_words:
        empty_trie.insert(word)
        assert empty_trie.search(word) == True
