def test_delete_existing_word(populated_trie):
    """Test deleting existing words"""
    assert populated_trie.search("cat") == True
    populated_trie.delete("cat")
    assert populated_trie.search("cat") == False
    assert populated_trie.search("cats") == True


def test_delete_existing_word_v2(populated_trie):
    """Test deleting existing words"""
    assert populated_trie.search("cat") == True
    populated_trie.delete("cats")
    assert populated_trie.search("cat") == True
    assert populated_trie.search("cats") == False
    assert populated_trie.search("catch") == True


def test_delete_empty_string(populated_trie):
    """Test deleting empty string"""
    initial_state = str(populated_trie.root)
    populated_trie.delete("")
    assert str(populated_trie.root) == initial_state


def test_delete_prefix_word(populated_trie):
    """Test deleting a word that is a prefix of another word"""
    populated_trie.delete("do")
    assert populated_trie.search("do") == False
    assert populated_trie.search("dog") == True
    assert populated_trie.search("dogs") == True
