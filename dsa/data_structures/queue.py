"""
Queue Implementations: FIFO Queue, Circular Queue, and Priority Queue.

Time Complexities:
- FIFO Queue Enqueue/Dequeue: O(1)
- Circular Queue Enqueue/Dequeue: O(1)
- Priority Queue Push/Pop: O(log n)
"""

import heapq
from typing import Any, List, Optional


class Queue:
    """FIFO Queue using Python list / double-ended indexing."""

    def __init__(self) -> None:
        self._items: List[Any] = []
        self._head_idx: int = 0

    def enqueue(self, item: Any) -> None:
        self._items.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Dequeue from empty queue.")
        item = self._items[self._head_idx]
        self._head_idx += 1
        # Re-index periodically to avoid unbounded memory expansion
        if self._head_idx > 1000 and self._head_idx > len(self._items) // 2:
            self._items = self._items[self._head_idx :]
            self._head_idx = 0
        return item

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from empty queue.")
        return self._items[self._head_idx]

    def is_empty(self) -> bool:
        return self._head_idx >= len(self._items)

    def __len__(self) -> int:
        return len(self._items) - self._head_idx


class CircularQueue:
    """Fixed-capacity Circular Queue using a fixed-size ring buffer."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self._capacity: int = capacity
        self._buffer: List[Optional[Any]] = [None] * capacity
        self._head: int = 0
        self._tail: int = 0
        self._size: int = 0

    def is_full(self) -> bool:
        return self._size == self._capacity

    def is_empty(self) -> bool:
        return self._size == 0

    def enqueue(self, value: Any) -> bool:
        if self.is_full():
            return False
        self._buffer[self._tail] = value
        self._tail = (self._tail + 1) % self._capacity
        self._size += 1
        return True

    def dequeue(self) -> Optional[Any]:
        if self.is_empty():
            return None
        val = self._buffer[self._head]
        self._buffer[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return val

    def front(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self._buffer[self._head]

    def rear(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self._buffer[(self._tail - 1 + self._capacity) % self._capacity]

    def __len__(self) -> int:
        return self._size


class PriorityQueue:
    """Min-Priority Queue using standard min-heap algorithm."""

    def __init__(self) -> None:
        self._heap: List[Any] = []

    def push(self, item: Any, priority: float) -> None:
        """Pushes item with priority (lower number = higher priority)."""
        heapq.heappush(self._heap, (priority, item))

    def pop(self) -> Any:
        """Pops and returns item with highest priority (lowest priority value)."""
        if self.is_empty():
            raise IndexError("Pop from empty PriorityQueue.")
        return heapq.heappop(self._heap)[1]

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from empty PriorityQueue.")
        return self._heap[0][1]

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def __len__(self) -> int:
        return len(self._heap)
