"""
Recursion and Divide-and-Conquer Algorithms.

Time Complexities:
- Fibonacci (Memoized): O(n) time, O(n) space
- Factorial: O(n) time, O(n) stack space
- Tower of Hanoi: O(2^n) time, O(n) stack space
- Subsets Generation: O(2^n) time, O(2^n) space
"""

from typing import Dict, List, Optional, Tuple


def fibonacci(n: int, memo: Optional[Dict[int, int]] = None) -> int:
    """
    Computes n-th Fibonacci number using top-down recursion with memoization.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n < 0:
        raise ValueError("n must be non-negative integer.")
    if n in (0, 1):
        return n

    if memo is None:
        memo = {}

    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]


def factorial(n: int) -> int:
    """
    Computes n! recursively.

    Time Complexity: O(n)
    Space Complexity: O(n) call stack
    """
    if n < 0:
        raise ValueError("n must be non-negative integer.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def tower_of_hanoi(
    n: int, source: str = "A", auxiliary: str = "B", target: str = "C"
) -> List[Tuple[str, str]]:
    """
    Solves Tower of Hanoi problem recursively for n disks.
    Returns list of moves as tuples: (from_peg, to_peg).

    Time Complexity: O(2^n)
    Space Complexity: O(n) stack space
    """
    moves: List[Tuple[str, str]] = []

    def _hanoi(disks: int, src: str, aux: str, tgt: str) -> None:
        if disks == 1:
            moves.append((src, tgt))
            return
        _hanoi(disks - 1, src, tgt, aux)
        moves.append((src, tgt))
        _hanoi(disks - 1, aux, src, tgt)

    if n > 0:
        _hanoi(n, source, auxiliary, target)
    return moves


def generate_subsets(nums: List[int]) -> List[List[int]]:
    """
    Generates power set (all subsets) of given set of integers.

    Time Complexity: O(2^n)
    Space Complexity: O(2^n)
    """
    subsets: List[List[int]] = []

    def _backtrack(index: int, current: List[int]) -> None:
        if index == len(nums):
            subsets.append(list(current))
            return

        # Include nums[index]
        current.append(nums[index])
        _backtrack(index + 1, current)
        current.pop()

        # Exclude nums[index]
        _backtrack(index + 1, current)

    _backtrack(0, [])
    return subsets
