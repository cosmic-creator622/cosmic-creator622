"""
Comprehensive Sorting Algorithms.

Time & Space Complexities:
- Bubble Sort: O(n^2) time, O(1) space
- Insertion Sort: O(n^2) time, O(1) space
- Selection Sort: O(n^2) time, O(1) space
- Merge Sort: O(n log n) time, O(n) space
- Quick Sort: O(n log n) avg, O(n^2) worst time, O(log n) space
- Heap Sort: O(n log n) time, O(1) space
- Counting Sort: O(n + k) time, O(k) space where k is range of elements
"""

from typing import List, TypeVar

T = TypeVar("T")


def bubble_sort(arr: List[int]) -> List[int]:
    """Bubble Sort with early termination optimization."""
    arr = list(arr)
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def insertion_sort(arr: List[int]) -> List[int]:
    """Insertion Sort."""
    arr = list(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr: List[int]) -> List[int]:
    """Selection Sort."""
    arr = list(arr)
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def merge_sort(arr: List[int]) -> List[int]:
    """Merge Sort divide-and-conquer implementation."""
    if len(arr) <= 1:
        return list(arr)

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: List[int]) -> List[int]:
    """Quick Sort using Lomuto partition scheme."""
    arr = list(arr)

    def _quick_sort(low: int, high: int) -> None:
        if low < high:
            p = _partition(low, high)
            _quick_sort(low, p - 1)
            _quick_sort(p + 1, high)

    def _partition(low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    _quick_sort(0, len(arr) - 1)
    return arr


def heap_sort(arr: List[int]) -> List[int]:
    """Heap Sort using in-place Max-Heap."""
    arr = list(arr)
    n = len(arr)

    def _heapify(n: int, i: int) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            _heapify(n, largest)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(i, 0)

    return arr


def counting_sort(arr: List[int]) -> List[int]:
    """Counting Sort for non-negative integer arrays."""
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val + 1

    count = [0] * range_val
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output
