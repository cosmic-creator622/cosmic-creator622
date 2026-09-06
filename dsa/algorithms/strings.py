"""
String Algorithms: KMP Pattern Matching, Rabin-Karp Rolling Hash, Palindrome, and Anagram Checking.

Time Complexities:
- KMP String Matching: O(N + M) time, O(M) space where N=text len, M=pattern len
- Rabin-Karp String Matching: O(N + M) avg time, O(1) space
- Is Palindrome: O(N) time, O(1) space
- Is Anagram: O(N) time, O(1) space (for fixed alphabet)
"""

from typing import List


def kmp_search(text: str, pattern: str) -> List[int]:
    """
    Knuth-Morris-Pratt (KMP) pattern matching algorithm.
    Finds all 0-based starting indices of pattern in text.

    Time Complexity: O(N + M)
    Space Complexity: O(M)
    """
    if not pattern or not text or len(pattern) > len(text):
        return []

    # Compute Longest Prefix Suffix (LPS) table
    lps = _compute_lps(pattern)
    matches = []

    i = 0  # index for text
    j = 0  # index for pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches


def _compute_lps(pattern: str) -> List[int]:
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def rabin_karp_search(text: str, pattern: str, prime: int = 101) -> List[int]:
    """
    Rabin-Karp pattern matching algorithm using rolling hash.

    Time Complexity: O(N + M) average, O(N * M) worst-case
    Space Complexity: O(1)
    """
    if not pattern or not text or len(pattern) > len(text):
        return []

    m = len(pattern)
    n = len(text)
    d = 256  # Number of characters in alphabet
    h = pow(d, m - 1, prime)

    p_hash = 0
    t_hash = 0
    matches = []

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i : i + m] == pattern:
                matches.append(i)

        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t_hash < 0:
                t_hash += prime

    return matches


def is_palindrome(s: str) -> bool:
    """
    Checks if string is palindrome (case-insensitive, alphanumeric only).

    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def is_anagram(s1: str, s2: str) -> bool:
    """
    Checks if s1 and s2 are anagrams.

    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if len(s1) != len(s2):
        return False

    count: dict = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1
    for char in s2:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True
