# DSA Algorithms & Data Structures Reference Library

An educational and production-grade Data Structures and Algorithms (DSA) library implemented in Python. This repository provides clean, fully tested, and thoroughly documented implementations of foundational computer science data structures and algorithmic paradigms with exact asymptotic time and space complexity analyses.

---

## Table of Contents
- [Problem Statement](#problem-statement)
- [Why This Project Exists](#why-this-project-exists)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Tech Stack](#tech-stack)
- [Setup & Usage](#setup--usage)
- [Data Structures & Algorithms Reference](#data-structures--algorithms-reference)
  - [Data Structures](#data-structures)
  - [Algorithms](#algorithms)
- [Testing](#testing)
- [Design Decisions](#design-decisions)
- [Challenges & Key Learnings](#challenges--key-learnings)
- [Limitations & Future Work](#limitations--future-work)

---

## Problem Statement

Understanding Data Structures and Algorithms is essential for software engineering, system design, and computer science problem-solving. While standard libraries provide high-level primitives (such as Python's built-in `list`, `dict`, and `heapq`), relying on abstractions without understanding their internal mechanics leads to sub-optimal architectural choices and inefficient code.

This project addresses the need for a unified, clean, and mathematically grounded reference library built from first principles.

---

## Why This Project Exists

1. **First-Principles Mastery**: Every component—from dynamic arrays and hash tables with collision handling to graph algorithms and dynamic programming—is written with explicit state management and complexity guarantees.
2. **Pedagogical Clarity**: Each module contains detailed docstrings explaining the underlying algorithm, step-by-step logic, edge cases, and runtime/space complexity.
3. **Engineered Standard**: Includes type hints, modular package design, clean separation of concerns, and 100% automated test coverage using Python's standard `unittest` runner.

---

## Features

- **Linear Data Structures**: Dynamic Array, Singly & Doubly Linked Lists, LIFO Stack, MinStack, Monotonic Stack, FIFO Queue, Circular Ring Buffer, Priority Queue.
- **Associative Structures**: Custom Hash Table with separate chaining collision resolution and dynamic rehashing on load factor threshold.
- **Tree & Graph Structures**: Binary Trees (with Pre/In/Post/Level-Order traversals), Binary Search Trees (with deletion and Lowest Common Ancestor), Min/Max Binary Heaps from scratch, Trie (Prefix Tree), Adjacency List Graph (BFS, DFS, Dijkstra, Topological Sort, Disjoint Set Union).
- **Fundamental & Advanced Algorithms**:
  - **Searching**: Linear, Iterative/Recursive Binary Search, Exponential Search, Ternary Search.
  - **Sorting**: Bubble, Insertion, Selection, Merge, Quick (Lomuto), Heap, and Counting Sort.
  - **Strings**: Knuth-Morris-Pratt (KMP) pattern matching, Rabin-Karp rolling hash, Palindrome, Anagram checks.
  - **Recursion & Backtracking**: Memoized Fibonacci, Factorial, Tower of Hanoi, N-Queens, Sudoku Solver, Permutations, Combination Sum.
  - **Greedy**: Fractional Knapsack, Activity Selection, Huffman Coding.
  - **Dynamic Programming**: 0/1 Knapsack, Longest Common Subsequence (LCS), Longest Increasing Subsequence (LIS), Coin Change (Min coins & combinations).

---

## Repository Structure

```text
dsa-algorithms/
├── dsa/
│   ├── __init__.py
│   ├── data_structures/
│   │   ├── __init__.py
│   │   ├── array.py               # Dynamic Array, Sliding Window, Two-Pointer utilities
│   │   ├── linked_list.py          # Singly/Doubly Linked Lists, Cycle Detection, Merge
│   │   ├── stack.py                # Stack, MinStack, Monotonic Stack, Valid Parentheses
│   │   ├── queue.py                # FIFO Queue, Circular Queue, Priority Queue
│   │   ├── hash_table.py           # Custom Hash Table with chaining & auto-resize
│   │   ├── tree.py                 # Binary Tree & Traversals
│   │   ├── bst.py                  # Binary Search Tree, Deletion, LCA
│   │   ├── heap.py                 # MinHeap & MaxHeap from scratch
│   │   ├── trie.py                 # Prefix Tree (Insert, Search, StartsWith, Delete)
│   │   └── graph.py                # Graph, BFS, DFS, Dijkstra, TopoSort, DisjointSet
│   └── algorithms/
│       ├── __init__.py
│       ├── searching.py            # Linear, Binary, Exponential, Ternary Search
│       ├── sorting.py              # Bubble, Insertion, Selection, Merge, Quick, Heap, Counting Sort
│       ├── strings.py              # KMP, Rabin-Karp, Palindrome, Anagram
│       ├── recursion.py            # Fibonacci, Factorial, Tower of Hanoi, Subsets
│       ├── greedy.py               # Fractional Knapsack, Activity Selection, Huffman Coding
│       ├── backtracking.py         # N-Queens, Sudoku Solver, Permutations, Combination Sum
│       └── dynamic_programming.py # 0/1 Knapsack, LCS, LIS, Coin Change
├── tests/
│   ├── __init__.py
│   ├── test_data_structures.py    # Unit tests for data structures
│   └── test_algorithms.py         # Unit tests for algorithms
├── .gitignore
└── README.md
```

---

## Tech Stack

- **Language**: Python 3.12+ (Type-annotated, standard library compliant)
- **Testing**: Python `unittest` framework

---

## Setup & Usage

### Prerequisites
Python 3.8+ installed on your system.

### Installation
Clone the repository:
```bash
git clone https://github.com/cosmic-creator622/dsa-algorithms.git
cd dsa-algorithms
```

### Quick Usage Example
```python
from dsa.data_structures.bst import BinarySearchTree
from dsa.algorithms.dynamic_programming import longest_common_subsequence
from dsa.algorithms.searching import binary_search

# Binary Search Tree Example
bst = BinarySearchTree()
for val in [10, 5, 15, 3, 7]:
    bst.insert(val)

print("In-order traversal:", bst.inorder())  # Output: [3, 5, 7, 10, 15]
print("LCA of 3 and 7:", bst.lowest_common_ancestor(3, 7))  # Output: 5

# Search Example
data = [2, 5, 8, 12, 16, 23, 38, 56]
idx = binary_search(data, 23)
print("Found 23 at index:", idx)  # Output: 5

# DP Example
lcs = longest_common_subsequence("AGGTAB", "GXTXAYB")
print("LCS:", lcs)  # Output: GTAB
```

---

## Data Structures & Algorithms Reference

### Data Structures

| Structure | Access | Search | Insertion | Deletion | Space Complexity |
|---|---|---|---|---|---|
| **Dynamic Array** | $O(1)$ | $O(n)$ | $O(1)$ amortized | $O(n)$ | $O(n)$ |
| **Singly Linked List** | $O(n)$ | $O(n)$ | $O(1)$ (head/tail) | $O(n)$ | $O(n)$ |
| **Doubly Linked List** | $O(n)$ | $O(n)$ | $O(1)$ (front/back) | $O(1)$ (known node) | $O(n)$ |
| **Stack** | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ | $O(n)$ |
| **MinStack** | $O(1)$ (top/min) | $O(n)$ | $O(1)$ | $O(1)$ | $O(n)$ |
| **Queue / Circular Queue** | $O(1)$ (front) | $O(n)$ | $O(1)$ | $O(1)$ | $O(n)$ |
| **Hash Table** | $N/A$ | $O(1)$ avg | $O(1)$ avg | $O(1)$ avg | $O(n)$ |
| **Binary Search Tree** | $O(h)$ | $O(h)$ | $O(h)$ | $O(h)$ | $O(n)$ |
| **Min/Max Binary Heap** | $O(1)$ (top) | $O(n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| **Trie (Prefix Tree)** | $N/A$ | $O(L)$ | $O(L)$ | $O(L)$ | $O(N \cdot L)$ |
| **Graph (Adjacency List)**| $N/A$ | $O(V + E)$ | $O(1)$ | $O(E)$ | $O(V + E)$ |

*Note: $h$ denotes tree height ($O(\log n)$ average, $O(n)$ worst-case). $L$ denotes string length.*

### Algorithms

| Algorithm | Category | Average Time | Worst Time | Space |
|---|---|---|---|---|
| **Binary Search** | Searching | $O(\log n)$ | $O(\log n)$ | $O(1)$ |
| **Exponential Search** | Searching | $O(\log n)$ | $O(\log n)$ | $O(1)$ |
| **Quick Sort** | Sorting | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ |
| **Merge Sort** | Sorting | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ |
| **Heap Sort** | Sorting | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ |
| **Counting Sort** | Sorting | $O(n + k)$ | $O(n + k)$ | $O(k)$ |
| **KMP Pattern Matching**| Strings | $O(N + M)$ | $O(N + M)$ | $O(M)$ |
| **Rabin-Karp Search** | Strings | $O(N + M)$ | $O(N \cdot M)$ | $O(1)$ |
| **Dijkstra Shortest Path**| Graph | $O((V + E) \log V)$ | $O((V + E) \log V)$| $O(V)$ |
| **Topological Sort** | Graph | $O(V + E)$ | $O(V + E)$ | $O(V)$ |
| **Disjoint Set (Union-Find)**| Graph | $O(\alpha(N))$ | $O(\alpha(N))$ | $O(N)$ |
| **Fractional Knapsack** | Greedy | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ |
| **Huffman Coding** | Greedy | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ |
| **N-Queens Solver** | Backtracking | $O(N!)$ | $O(N!)$ | $O(N^2)$ |
| **0/1 Knapsack** | DP | $O(N \cdot W)$ | $O(N \cdot W)$ | $O(W)$ |
| **LCS** | DP | $O(M \cdot N)$ | $O(M \cdot N)$ | $O(M \cdot N)$ |
| **LIS** | DP | $O(N \log N)$ | $O(N \log N)$ | $O(N)$ |

---

## Testing

Run all unit tests via Python's standard `unittest` test discovery:

```bash
python3 -m unittest discover tests
```

To run individual test suites:
```bash
python3 -m unittest tests/test_data_structures.py
python3 -m unittest tests/test_algorithms.py
```

---

## Design Decisions

1. **Pure Python Standard Library Compliance**: Avoided unnecessary external dependencies (like numpy or third-party graph frameworks) to keep the core algorithms transparent, portable, and easy to inspect.
2. **Explict Memory & Array Invariants**: Implemented array resizing, circular queue buffers, and binary heaps using explicit index math rather than wrapping existing higher-level primitives.
3. **Disjoint Set Union Optimizations**: Implemented both path compression in `find()` and rank-based heuristics in `union()` to achieve near O(1) amortized inverse Ackermann time complexity.

---

## Challenges & Key Learnings

- **Hash Table Collision Handling**: Balancing load factor threshold (0.75) and dynamic resizing during chaining requires careful iterator pointer updates.
- **BST Node Deletion**: Handling the case of deleting a node with two children by swapping with its in-order successor (minimum node in the right subtree) requires maintaining tree pointer invariants.
- **KMP Prefix Function**: Computing the Longest Prefix Suffix (LPS) table correctly avoids redundant backtracks during string matching.

---

## Limitations & Future Work

- **Self-Balancing Trees**: AVL Trees or Red-Black Trees could be added to guarantee $O(\log n)$ worst-case BST height.
- **Advanced Graph Algorithms**: Tarjan's Strongly Connected Components and Prim's/Kruskal's Minimum Spanning Tree can further expand graph capability.
