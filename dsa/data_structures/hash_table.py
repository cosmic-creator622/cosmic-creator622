"""
Custom Hash Table Implementation with Separate Chaining.

Features:
- Custom hash function using polynomial rolling hash / python hash
- Separate chaining collision resolution with linked bucket lists
- Dynamic resizing when load factor exceeds threshold (0.75)

Time Complexities:
- Insert: O(1) average, O(n) worst-case
- Search: O(1) average, O(n) worst-case
- Delete: O(1) average, O(n) worst-case
Space Complexity: O(n)
"""

from typing import Any, List, Optional, Tuple


class HashNode:
    def __init__(self, key: Any, value: Any, next_node: Optional["HashNode"] = None) -> None:
        self.key: Any = key
        self.value: Any = value
        self.next: Optional["HashNode"] = next_node


class HashTable:
    """
    Hash Table using separate chaining for collision resolution.
    """

    def __init__(self, initial_capacity: int = 16, load_factor_threshold: float = 0.75) -> None:
        if initial_capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self._capacity: int = initial_capacity
        self._load_factor_threshold: float = load_factor_threshold
        self._size: int = 0
        self._buckets: List[Optional[HashNode]] = [None] * self._capacity

    def __len__(self) -> int:
        return self._size

    def _hash(self, key: Any) -> int:
        """Computes bucket index for a given key."""
        return hash(key) % self._capacity

    def _resize(self, new_capacity: int) -> None:
        """Resizes bucket array and rehashes all items."""
        old_buckets = self._buckets
        self._capacity = new_capacity
        self._buckets = [None] * self._capacity
        self._size = 0

        for head in old_buckets:
            curr = head
            while curr:
                self.put(curr.key, curr.value)
                curr = curr.next

    def put(self, key: Any, value: Any) -> None:
        """Inserts or updates key-value pair."""
        if (self._size + 1) / self._capacity > self._load_factor_threshold:
            self._resize(self._capacity * 2)

        idx = self._hash(key)
        head = self._buckets[idx]

        curr = head
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next

        new_node = HashNode(key, value, head)
        self._buckets[idx] = new_node
        self._size += 1

    def get(self, key: Any, default: Any = None) -> Any:
        """Retrieves value associated with key, or default if key not found."""
        idx = self._hash(key)
        curr = self._buckets[idx]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return default

    def remove(self, key: Any) -> bool:
        """Removes key-value pair. Returns True if key was present."""
        idx = self._hash(key)
        curr = self._buckets[idx]
        prev: Optional[HashNode] = None

        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self._buckets[idx] = curr.next
                self._size -= 1
                return True
            prev = curr
            curr = curr.next

        return False

    def contains(self, key: Any) -> bool:
        """Checks if key is present in hash table."""
        return self.get(key) is not None

    def __getitem__(self, key: Any) -> Any:
        val = self.get(key)
        if val is None and not self.contains(key):
            raise KeyError(key)
        return val

    def __setitem__(self, key: Any, value: Any) -> None:
        self.put(key, value)

    def __delitem__(self, key: Any) -> None:
        if not self.remove(key):
            raise KeyError(key)

    def keys(self) -> List[Any]:
        result = []
        for head in self._buckets:
            curr = head
            while curr:
                result.append(curr.key)
                curr = curr.next
        return result

    def values(self) -> List[Any]:
        result = []
        for head in self._buckets:
            curr = head
            while curr:
                result.append(curr.value)
                curr = curr.next
        return result
