"""
Greedy Algorithms: Fractional Knapsack, Activity Selection, and Huffman Coding.

Time Complexities:
- Fractional Knapsack: O(n log n)
- Activity Selection: O(n log n)
- Huffman Coding: O(n log n)
"""

import heapq
from typing import Dict, List, Optional, Tuple


class HuffmanNode:
    def __init__(self, char: Optional[str], freq: int) -> None:
        self.char: Optional[str] = char
        self.freq: int = freq
        self.left: Optional["HuffmanNode"] = None
        self.right: Optional["HuffmanNode"] = None

    def __lt__(self, other: "HuffmanNode") -> bool:
        return self.freq < other.freq


def fractional_knapsack(weights: List[float], values: List[float], capacity: float) -> float:
    """
    Solves Fractional Knapsack problem using Greedy strategy (sort by value/weight ratio).

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(weights) != len(values) or capacity <= 0:
        return 0.0

    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]
    items.sort(key=lambda x: x[0], reverse=True)

    total_value = 0.0
    current_capacity = capacity

    for ratio, weight, value in items:
        if current_capacity <= 0:
            break
        if weight <= current_capacity:
            total_value += value
            current_capacity -= weight
        else:
            total_value += ratio * current_capacity
            current_capacity = 0.0

    return total_value


def activity_selection(start_times: List[int], finish_times: List[int]) -> List[int]:
    """
    Selects maximum number of mutually compatible activities.
    Returns list of indices of selected activities.

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(start_times) != len(finish_times) or not start_times:
        return []

    activities = [(start_times[i], finish_times[i], i) for i in range(len(start_times))]
    activities.sort(key=lambda x: x[1])  # Sort by finish time

    selected_indices = [activities[0][2]]
    last_finish = activities[0][1]

    for i in range(1, len(activities)):
        start, finish, idx = activities[i]
        if start >= last_finish:
            selected_indices.append(idx)
            last_finish = finish

    return selected_indices


def build_huffman_tree(text: str) -> Tuple[Optional[HuffmanNode], Dict[str, str]]:
    """
    Builds Huffman Tree for text compression and generates variable-length prefix codes.

    Returns (root_node, code_map).

    Time Complexity: O(n log n) where n is unique character count
    Space Complexity: O(n)
    """
    if not text:
        return None, {}

    # Calculate frequencies
    freq_map: Dict[str, int] = {}
    for char in text:
        freq_map[char] = freq_map.get(char, 0) + 1

    # Priority queue of nodes
    heap: List[HuffmanNode] = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        root = HuffmanNode(None, heap[0].freq)
        root.left = heap[0]
        return root, {heap[0].char: "0"}

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    root = heap[0]
    code_map: Dict[str, str] = {}

    def _generate_codes(node: Optional[HuffmanNode], current_code: str) -> None:
        if not node:
            return
        if node.char is not None:
            code_map[node.char] = current_code
            return
        _generate_codes(node.left, current_code + "0")
        _generate_codes(node.right, current_code + "1")

    _generate_codes(root, "")
    return root, code_map
