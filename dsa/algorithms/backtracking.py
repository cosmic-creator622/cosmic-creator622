"""
Backtracking Algorithms: N-Queens, Sudoku Solver, Permutations, and Combination Sum.

Time Complexities:
- N-Queens: O(N!)
- Sudoku Solver: O(9^(N*N))
- Permutations: O(N * N!)
- Combination Sum: O(2^T) where T is target
"""

from typing import List, Set


def solve_n_queens(n: int) -> List[List[str]]:
    """
    Solves N-Queens problem on N x N chessboard using backtracking.
    Returns list of all distinct solutions represented as lists of strings.

    Time Complexity: O(N!)
    Space Complexity: O(N^2)
    """
    solutions: List[List[str]] = []
    cols: Set[int] = set()
    pos_diag: Set[int] = set()  # (r + c)
    neg_diag: Set[int] = set()  # (r - c)

    board = [["."] * n for _ in range(n)]

    def _backtrack(r: int) -> None:
        if r == n:
            solutions.append(["".join(row) for row in board])
            return

        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"

            _backtrack(r + 1)

            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."

    _backtrack(0)
    return solutions


def solve_sudoku(board: List[List[str]]) -> bool:
    """
    Solves 9x9 Sudoku puzzle in-place using backtracking.
    '.' represents empty cell. Returns True if solvable.

    Time Complexity: O(9^(empty_cells))
    Space Complexity: O(1) auxiliary
    """

    def _is_valid(r: int, c: int, char: str) -> bool:
        for i in range(9):
            if board[r][i] == char or board[i][c] == char:
                return False
            subgrid_r = 3 * (r // 3) + i // 3
            subgrid_c = 3 * (c // 3) + i % 3
            if board[subgrid_r][subgrid_c] == char:
                return False
        return True

    def _solve() -> bool:
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for digit in "123456789":
                        if _is_valid(r, c, digit):
                            board[r][c] = digit
                            if _solve():
                                return True
                            board[r][c] = "."
                    return False
        return True

    return _solve()


def permute(nums: List[int]) -> List[List[int]]:
    """
    Generates all unique permutations of list of numbers using backtracking.

    Time Complexity: O(N * N!)
    Space Complexity: O(N * N!)
    """
    results: List[List[int]] = []

    def _backtrack(start: int) -> None:
        if start == len(nums):
            results.append(list(nums))
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            _backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    _backtrack(0)
    return results


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Finds all unique combinations in candidates where candidate numbers sum to target.
    Candidates can be chosen unlimited times.

    Time Complexity: O(2^T)
    Space Complexity: O(T)
    """
    results: List[List[int]] = []
    candidates.sort()

    def _backtrack(remain: int, combo: List[int], start: int) -> None:
        if remain == 0:
            results.append(list(combo))
            return

        for i in range(start, len(candidates)):
            num = candidates[i]
            if num > remain:
                break
            combo.append(num)
            _backtrack(remain - num, combo, i)
            combo.pop()

    _backtrack(target, [], 0)
    return results
