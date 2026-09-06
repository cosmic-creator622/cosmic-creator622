"""
Unit tests for Algorithms.
"""

import unittest

from dsa.algorithms.backtracking import (
    combination_sum,
    permute,
    solve_n_queens,
    solve_sudoku,
)
from dsa.algorithms.dynamic_programming import (
    coin_change_min,
    coin_change_ways,
    knapsack_01,
    longest_common_subsequence,
    longest_increasing_subsequence,
)
from dsa.algorithms.greedy import activity_selection, build_huffman_tree, fractional_knapsack
from dsa.algorithms.recursion import factorial, fibonacci, generate_subsets, tower_of_hanoi
from dsa.algorithms.searching import (
    binary_search,
    binary_search_recursive,
    exponential_search,
    linear_search,
    ternary_search,
)
from dsa.algorithms.sorting import (
    bubble_sort,
    counting_sort,
    heap_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort,
)
from dsa.algorithms.strings import is_anagram, is_palindrome, kmp_search, rabin_karp_search


class TestSearching(unittest.TestCase):
    def setUp(self) -> None:
        self.sorted_arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

    def test_searching_algorithms(self) -> None:
        target = 23
        self.assertEqual(linear_search(self.sorted_arr, target), 5)
        self.assertEqual(binary_search(self.sorted_arr, target), 5)
        self.assertEqual(binary_search_recursive(self.sorted_arr, target), 5)
        self.assertEqual(exponential_search(self.sorted_arr, target), 5)
        self.assertEqual(ternary_search(self.sorted_arr, target), 5)

        missing = 100
        self.assertIsNone(linear_search(self.sorted_arr, missing))
        self.assertIsNone(binary_search(self.sorted_arr, missing))
        self.assertIsNone(exponential_search(self.sorted_arr, missing))
        self.assertIsNone(ternary_search(self.sorted_arr, missing))


class TestSorting(unittest.TestCase):
    def setUp(self) -> None:
        self.unsorted = [64, 34, 25, 12, 22, 11, 90]
        self.expected = [11, 12, 22, 25, 34, 64, 90]

    def test_sorting_algorithms(self) -> None:
        self.assertEqual(bubble_sort(self.unsorted), self.expected)
        self.assertEqual(insertion_sort(self.unsorted), self.expected)
        self.assertEqual(selection_sort(self.unsorted), self.expected)
        self.assertEqual(merge_sort(self.unsorted), self.expected)
        self.assertEqual(quick_sort(self.unsorted), self.expected)
        self.assertEqual(heap_sort(self.unsorted), self.expected)
        self.assertEqual(counting_sort(self.unsorted), self.expected)


class TestStrings(unittest.TestCase):
    def test_kmp_and_rabin_karp(self) -> None:
        text = "AABAACAADAABAABA"
        pattern = "AABA"
        expected = [0, 9, 12]

        self.assertEqual(kmp_search(text, pattern), expected)
        self.assertEqual(rabin_karp_search(text, pattern), expected)

    def test_palindrome_and_anagram(self) -> None:
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("race a car"))

        self.assertTrue(is_anagram("listen", "silent"))
        self.assertFalse(is_anagram("hello", "billion"))


class TestRecursion(unittest.TestCase):
    def test_fibonacci_and_factorial(self) -> None:
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(factorial(5), 120)

    def test_hanoi_and_subsets(self) -> None:
        moves = tower_of_hanoi(3)
        self.assertEqual(len(moves), 7)  # 2^3 - 1 = 7

        subsets = generate_subsets([1, 2])
        self.assertEqual(len(subsets), 4)


class TestGreedy(unittest.TestCase):
    def test_fractional_knapsack(self) -> None:
        weights = [10.0, 20.0, 30.0]
        values = [60.0, 100.0, 120.0]
        capacity = 50.0
        # 10kg item1 (60) + 20kg item2 (100) + 20kg of item3 (80) = 240
        self.assertEqual(fractional_knapsack(weights, values, capacity), 240.0)

    def test_activity_selection(self) -> None:
        start = [1, 3, 0, 5, 8, 5]
        finish = [2, 4, 6, 7, 9, 9]
        selected = activity_selection(start, finish)
        self.assertEqual(len(selected), 4)

    def test_huffman_coding(self) -> None:
        text = "abracadabra"
        root, codes = build_huffman_tree(text)
        self.assertIsNotNone(root)
        self.assertEqual(len(codes), len(set(text)))


class TestBacktracking(unittest.TestCase):
    def test_n_queens(self) -> None:
        solutions_4 = solve_n_queens(4)
        self.assertEqual(len(solutions_4), 2)

    def test_sudoku_solver(self) -> None:
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertTrue(solve_sudoku(board))
        self.assertEqual(board[0][2], "4")

    def test_permute_and_combination_sum(self) -> None:
        perms = permute([1, 2, 3])
        self.assertEqual(len(perms), 6)

        combs = combination_sum([2, 3, 6, 7], 7)
        self.assertIn([7], combs)
        self.assertIn([2, 2, 3], combs)


class TestDynamicProgramming(unittest.TestCase):
    def test_knapsack_01(self) -> None:
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 50
        self.assertEqual(knapsack_01(weights, values, capacity), 220)

    def test_lcs_and_lis(self) -> None:
        self.assertEqual(longest_common_subsequence("AGGTAB", "GXTXAYB"), "GTAB")
        self.assertEqual(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_coin_change(self) -> None:
        self.assertEqual(coin_change_min([1, 2, 5], 11), 3)  # 5 + 5 + 1
        self.assertEqual(coin_change_ways([1, 2, 5], 5), 4)


if __name__ == "__main__":
    unittest.main()
