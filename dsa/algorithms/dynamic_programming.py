"""
Dynamic Programming Algorithms: 0/1 Knapsack, LCS, LIS, and Coin Change.

Time & Space Complexities:
- 0/1 Knapsack: O(N * W) time, O(N * W) space (can be optimized to O(W) space)
- Longest Common Subsequence (LCS): O(M * N) time, O(M * N) space
- Longest Increasing Subsequence (LIS): O(N^2) DP or O(N log N) binary search
- Coin Change Min: O(Amount * N) time, O(Amount) space
- Coin Change Ways: O(Amount * N) time, O(Amount) space
"""

from typing import List


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """
    0/1 Knapsack problem using Bottom-Up Dynamic Programming.

    Time Complexity: O(N * W) where N is items count, W is capacity
    Space Complexity: O(W) space optimized
    """
    if not weights or len(weights) != len(values) or capacity <= 0:
        return 0

    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        w = weights[i]
        v = values[i]
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)

    return dp[capacity]


def longest_common_subsequence(s1: str, s2: str) -> str:
    """
    Finds Longest Common Subsequence (LCS) of strings s1 and s2.

    Time Complexity: O(M * N)
    Space Complexity: O(M * N)
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct LCS string
    lcs_chars = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_chars.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs_chars))


def longest_increasing_subsequence(nums: List[int]) -> int:
    """
    Finds length of Longest Increasing Subsequence (LIS) in O(N log N) using binary search DP.

    Time Complexity: O(N log N)
    Space Complexity: O(N)
    """
    if not nums:
        return 0

    tails: List[int] = []

    for x in nums:
        # Binary search for x in tails
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < x:
                left = mid + 1
            else:
                right = mid

        if left == len(tails):
            tails.append(x)
        else:
            tails[left] = x

    return len(tails)


def coin_change_min(coins: List[int], amount: int) -> int:
    """
    Finds fewest number of coins needed to make up given amount.
    Returns -1 if amount cannot be made up.

    Time Complexity: O(Amount * N)
    Space Complexity: O(Amount)
    """
    if amount == 0:
        return 0

    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return int(dp[amount]) if dp[amount] != float("inf") else -1


def coin_change_ways(coins: List[int], amount: int) -> int:
    """
    Finds number of combinations that make up given amount.

    Time Complexity: O(Amount * N)
    Space Complexity: O(Amount)
    """
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]
