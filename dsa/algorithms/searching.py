"""
Searching Algorithms: Linear Search, Binary Search, Exponential Search, and Ternary Search.

Time Complexities:
- Linear Search: O(n)
- Binary Search: O(log n)
- Exponential Search: O(log n)
- Ternary Search: O(log_3 n) = O(log n)
"""

from typing import List, Optional, TypeVar

T = TypeVar("T")


def linear_search(arr: List[T], target: T) -> Optional[int]:
    """
    Linear Search: Iterates over array to find index of target.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i, item in enumerate(arr):
        if item == target:
            return i
    return None


def binary_search(arr: List[T], target: T) -> Optional[int]:
    """
    Iterative Binary Search on a sorted array.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


def binary_search_recursive(
    arr: List[T], target: T, low: int = 0, high: Optional[int] = None
) -> Optional[int]:
    """
    Recursive Binary Search on a sorted array.

    Time Complexity: O(log n)
    Space Complexity: O(log n) call stack
    """
    if high is None:
        high = len(arr) - 1

    if low > high:
        return None

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


def exponential_search(arr: List[T], target: T) -> Optional[int]:
    """
    Exponential Search for unbounded or large sorted arrays.
    Finds range where target exists, then performs binary search.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    if not arr:
        return None
    if arr[0] == target:
        return 0

    n = len(arr)
    bound = 1
    while bound < n and arr[bound] <= target:
        bound *= 2

    # Binary search within range [bound//2, min(bound, n - 1)]
    low = bound // 2
    high = min(bound, n - 1)

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


def ternary_search(arr: List[T], target: T) -> Optional[int]:
    """
    Ternary Search divides array into 3 parts instead of 2.

    Time Complexity: O(log_3 n)
    Space Complexity: O(1)
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            high = mid1 - 1
        elif target > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1

    return None
