"""
Stack Implementations and Monotonic Stack Algorithms.

Time Complexities:
- Push / Pop / Peek: O(1)
- MinStack Get Min: O(1)
- Monotonic Stack Next Greater Element: O(n)
- Valid Parentheses Check: O(n) time, O(n) space
"""

from typing import Any, List, Optional, Tuple


class Stack:
    """LIFO Stack implementation using Python list."""

    def __init__(self) -> None:
        self._items: List[Any] = []

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Pop from empty stack.")
        return self._items.pop()

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from empty stack.")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)


class MinStack:
    """
    Stack that retrieves minimum element in O(1) time.
    Maintains a secondary stack tracking minimum values.
    """

    def __init__(self) -> None:
        self._stack: List[int] = []
        self._min_stack: List[int] = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self) -> int:
        if not self._stack:
            raise IndexError("Pop from empty MinStack.")
        val = self._stack.pop()
        if val == self._min_stack[-1]:
            self._min_stack.pop()
        return val

    def top(self) -> int:
        if not self._stack:
            raise IndexError("Top from empty MinStack.")
        return self._stack[-1]

    def get_min(self) -> int:
        if not self._min_stack:
            raise IndexError("Get min from empty MinStack.")
        return self._min_stack[-1]


def next_greater_element(arr: List[int]) -> List[int]:
    """
    Finds next greater element for each item in array using a monotonic stack.
    Returns array where index i contains next greater element or -1 if none exists.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(arr)
    result = [-1] * n
    stack: List[int] = []  # Store indices

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)

    return result


def is_valid_parentheses(s: str) -> bool:
    """
    Validates if string of brackets '()[]{}' is balanced using a stack.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    bracket_map = {')': '(', ']': '[', '}': '{'}
    stack: List[str] = []

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False
        else:
            # Ignore non-bracket characters if any
            pass

    return len(stack) == 0
