def test_search_existing_word(populated_trie):
    """Test searching for words that exist in the trie"""
    assert populated_trie.search("cat") == True
    assert populated_trie.search("cats") == True
    assert populated_trie.search("catch") == True


def test_search_nonexistent_word(populated_trie):
    """Test searching for words that don't exist in the trie"""
    assert populated_trie.search("cap") == False
    assert populated_trie.search("cat!") == False
    assert populated_trie.search("ca") == False
    assert populated_trie.search("catches") == False


def test_search_empty_string(populated_trie):
    """Test searching for an empty string"""
    assert populated_trie.search("") == False
