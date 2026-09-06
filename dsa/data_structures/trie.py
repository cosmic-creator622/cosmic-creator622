"""
Trie (Prefix Tree) Implementation.

Time Complexities:
- Insert: O(L) where L is length of word
- Search: O(L)
- StartsWith: O(L)
- Delete: O(L)
Space Complexity: O(N * L) where N is number of words
"""

from typing import Dict, Optional


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False


class Trie:
    """Prefix Tree for efficient string retrieval and autocomplete operations."""

    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts word into trie."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Returns True if word is in trie."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Returns True if there is any word in trie starting with prefix."""
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

    def delete(self, word: str) -> bool:
        """Deletes word from trie if present. Returns True if deleted."""

        def _delete(node: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                if not node.is_end_of_word:
                    return False  # Word not found
                node.is_end_of_word = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            should_delete_child = _delete(node.children[char], word, index + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word

            return False

        if not self.search(word):
            return False
        _delete(self.root, word, 0)
        return True
