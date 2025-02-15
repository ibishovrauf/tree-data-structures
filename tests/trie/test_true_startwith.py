def test_starts_with_existing_prefix(populated_trie):
    """Test startsWith for existing prefixes"""
    assert populated_trie.startsWith("cat") == True
    assert populated_trie.startsWith("do") == True
    assert populated_trie.startsWith("c") == True


def test_starts_with_nonexistent_prefix(populated_trie):
    """Test startsWith for non-existing prefixes"""
    assert populated_trie.startsWith("cap") == False
    assert populated_trie.startsWith("top") == False


def test_starts_with_empty_string(populated_trie):
    """Test startsWith with empty string"""
    assert populated_trie.startsWith("") == True
