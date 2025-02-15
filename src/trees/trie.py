from typing import Any, Optional, AnyStr

from src.nodes.trie_node import TrieNode


class Trie:

    def __init__(self) -> None:
        self._root = None

    def insert(self, value: AnyStr) -> None:
        if not isinstance(value, str):
            raise TypeError("Inserted value must be a string")

        if not self._root:
            self._root = TrieNode(None)

        prev = self._root
        for char in value:
            if char not in prev.children.keys():
                prev.add_child({char: TrieNode(char)})
            prev = prev.children[char]
        prev.wordEnd = True

    def search(self, value: AnyStr) -> bool:
        if not isinstance(value, str):
            raise TypeError("Inserted value must be a string")

        if not self.root:
            return False

        if not value:
            return False

        curr = self.root
        for char in value:
            curr = curr.children.get(char)
            if not curr:
                return False
        return curr.wordEnd

    def startsWith(self, value: AnyStr) -> bool:
        if not isinstance(value, str):
            raise TypeError("Inserted value must be a string")

        if not self.root:
            return False

        if not value:
            return bool(self.root.children)

        curr = self.root
        for char in value:
            curr = curr.children.get(char)
            if not curr:
                return False
        return True

    def delete(self, value: Any) -> None:
        if not isinstance(value, str):
            raise TypeError("Inserted value must be a string")

        if not self.root:
            raise ValueError()

        if not value:
            return

        path = [self.root]
        curr = self.root
        for char in value:
            curr = curr.children.get(char)
            path.append(curr)
            if not curr:
                raise ValueError()
        
        if not curr.wordEnd:
            raise ValueError()
        
        if curr.child_count != 0:
            curr.wordEnd = False
            return
        
        path.reverse()
        for index, element in enumerate(path):
            if element.child_count > 1:
                break
        del path[index].children[path[index-1].value]
        return 

    @property
    def root(self):
        return self._root

    def __str__(self) -> str:
        return str(self.root)
