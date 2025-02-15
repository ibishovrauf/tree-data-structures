def test_init(empty_trie):
    """Test initialization of empty Trie"""
    assert empty_trie.root is None


def test_insert_single_word(empty_trie):
    """Test inserting a single word"""
    empty_trie.insert("salam")
    assert empty_trie.root.value is None
    assert empty_trie.root.children["s"].children["a"].children["l"].children[
        "a"].children["m"].wordEnd == True


def test_insert_multiple_words(empty_trie):
    """Test inserting multiple words with common prefix"""
    empty_trie.insert("salam")
    empty_trie.insert("salm")

    assert empty_trie.root.value is None
    assert empty_trie.root.children["s"].children["a"].children["l"].children[
        "a"].children["m"].wordEnd == True
    assert empty_trie.root.children["s"].children["a"].children["l"].children[
        "m"].wordEnd == True


def test_insert_empty_string(empty_trie):
    """Test inserting an empty string"""
    empty_trie.insert("")
    print(empty_trie.root.children == {})
    assert empty_trie.root.children == {}
