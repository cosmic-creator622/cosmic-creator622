"""
Dynamic Array and Array Algorithm Patterns.

Time Complexities:
- Dynamic Array Access: O(1)
- Dynamic Array Append: O(1) amortized, O(n) worst-case (during resize)
- Dynamic Array Insert/Delete: O(n)
- Sliding Window (Max Subarray Sum K): O(n) time, O(1) space
- Two Pointers (Two Sum Sorted): O(n) time, O(1) space
"""

from typing import Any, List, Optional, Tuple


class DynamicArray:
    """
    A resizable array implementation demonstrating dynamic memory allocation concepts.

    Attributes:
        capacity (int): The maximum number of elements before resizing.
        length (int): The current number of elements stored.
    """

    def __init__(self, initial_capacity: int = 10) -> None:
        if initial_capacity <= 0:
            raise ValueError("Initial capacity must be greater than 0.")
        self._capacity: int = initial_capacity
        self._length: int = 0
        self._data: List[Optional[Any]] = [None] * self._capacity

    def __len__(self) -> int:
        return self._length

    def __getitem__(self, index: int) -> Any:
        self._validate_index(index)
        return self._data[index]

    def __setitem__(self, index: int, value: Any) -> None:
        self._validate_index(index)
        self._data[index] = value

    def _validate_index(self, index: int) -> None:
        if not (0 <= index < self._length):
            raise IndexError(f"Index {index} out of bounds for array of size {self._length}.")

    def _resize(self, new_capacity: int) -> None:
        """Resizes the internal array buffer to new_capacity."""
        new_data: List[Optional[Any]] = [None] * new_capacity
        for i in range(self._length):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, value: Any) -> None:
        """Appends value to the end of array, doubling capacity if full."""
        if self._length == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._length] = value
        self._length += 1

    def pop(self) -> Any:
        """Removes and returns the last element."""
        if self._length == 0:
            raise IndexError("Pop from empty array.")
        val = self._data[self._length - 1]
        self._data[self._length - 1] = None
        self._length -= 1
        if 0 < self._length <= self._capacity // 4 and self._capacity // 2 >= 10:
            self._resize(self._capacity // 2)
        return val

    def insert(self, index: int, value: Any) -> None:
        """Inserts value at given index."""
        if not (0 <= index <= self._length):
            raise IndexError(f"Index {index} out of bounds.")
        if self._length == self._capacity:
            self._resize(self._capacity * 2)
        for i in range(self._length, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._length += 1

    def delete(self, index: int) -> Any:
        """Deletes item at index and returns it."""
        self._validate_index(index)
        val = self._data[index]
        for i in range(index, self._length - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._length - 1] = None
        self._length -= 1
        return val

    def to_list(self) -> List[Any]:
        """Returns Python list of elements."""
        return [self._data[i] for i in range(self._length)]


def max_sub_array_sum_k(arr: List[int], k: int) -> Optional[int]:
    """
    Finds maximum sum of contiguous subarray of size k using sliding window.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(arr) < k or k <= 0:
        return None

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def two_sum_sorted(arr: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Finds pair of indices (0-indexed) whose values sum to target in a sorted array using two-pointer technique.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return left, right
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None
