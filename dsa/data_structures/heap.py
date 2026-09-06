"""
Binary Heap Implementations (MinHeap and MaxHeap) built from scratch.

Array index relationships:
- Left child: 2 * i + 1
- Right child: 2 * i + 2
- Parent: (i - 1) // 2

Time Complexities:
- Insert: O(log n)
- Extract Min/Max: O(log n)
- Peek: O(1)
- Build Heap (Heapify list): O(n)
"""

from typing import Any, List, Optional


class MinHeap:
    """Min-Heap implementation from scratch."""

    def __init__(self, elements: Optional[List[Any]] = None) -> None:
        self.heap: List[Any] = []
        if elements:
            self.heap = list(elements)
            self._build_heap()

    def __len__(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from empty heap.")
        return self.heap[0]

    def insert(self, value: Any) -> None:
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self) -> Any:
        if self.is_empty():
            raise IndexError("Extract from empty heap.")
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index: int) -> None:
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index: int) -> None:
        size = len(self.heap)
        smallest = index

        while True:
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def _build_heap(self) -> None:
        """Floyd's heap construction algorithm O(n)."""
        for i in range((len(self.heap) - 2) // 2, -1, -1):
            self._heapify_down(i)


class MaxHeap:
    """Max-Heap implementation from scratch."""

    def __init__(self, elements: Optional[List[Any]] = None) -> None:
        self.heap: List[Any] = []
        if elements:
            self.heap = list(elements)
            self._build_heap()

    def __len__(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from empty heap.")
        return self.heap[0]

    def insert(self, value: Any) -> None:
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self) -> Any:
        if self.is_empty():
            raise IndexError("Extract from empty heap.")
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index: int) -> None:
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index: int) -> None:
        size = len(self.heap)
        largest = index

        while True:
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def _build_heap(self) -> None:
        for i in range((len(self.heap) - 2) // 2, -1, -1):
            self._heapify_down(i)
