"""
Unit tests for Data Structures.
"""

import unittest

from dsa.data_structures.array import DynamicArray, max_sub_array_sum_k, two_sum_sorted
from dsa.data_structures.bst import BinarySearchTree
from dsa.data_structures.graph import DisjointSet, Graph, bfs, dfs, dijkstra, topological_sort
from dsa.data_structures.hash_table import HashTable
from dsa.data_structures.heap import MaxHeap, MinHeap
from dsa.data_structures.linked_list import (
    DoublyLinkedList,
    SinglyLinkedList,
    SinglyNode,
    detect_cycle_floyd,
    merge_two_sorted_lists,
)
from dsa.data_structures.queue import CircularQueue, PriorityQueue, Queue
from dsa.data_structures.stack import MinStack, Stack, is_valid_parentheses, next_greater_element
from dsa.data_structures.tree import BinaryTree, BinaryTreeNode
from dsa.data_structures.trie import Trie


class TestDynamicArray(unittest.TestCase):
    def test_array_operations(self) -> None:
        arr = DynamicArray(initial_capacity=2)
        self.assertEqual(len(arr), 0)

        arr.append(10)
        arr.append(20)
        arr.append(30)  # Should trigger resize
        self.assertEqual(len(arr), 3)
        self.assertEqual(arr[0], 10)
        self.assertEqual(arr[1], 20)
        self.assertEqual(arr[2], 30)

        arr[1] = 25
        self.assertEqual(arr[1], 25)

        popped = arr.pop()
        self.assertEqual(popped, 30)
        self.assertEqual(len(arr), 2)

        arr.insert(1, 15)
        self.assertEqual(arr.to_list(), [10, 15, 25])

        deleted = arr.delete(0)
        self.assertEqual(deleted, 10)
        self.assertEqual(arr.to_list(), [15, 25])

    def test_array_bounds_exception(self) -> None:
        arr = DynamicArray()
        with self.assertRaises(IndexError):
            _ = arr[0]
        with self.assertRaises(IndexError):
            arr.pop()

    def test_sliding_window_and_two_pointers(self) -> None:
        self.assertEqual(max_sub_array_sum_k([2, 1, 5, 1, 3, 2], 3), 9)
        self.assertIsNone(max_sub_array_sum_k([1, 2], 3))

        self.assertEqual(two_sum_sorted([1, 2, 4, 6, 8, 11], 10), (1, 4))
        self.assertIsNone(two_sum_sorted([1, 2, 3], 10))


class TestLinkedLists(unittest.TestCase):
    def test_singly_linked_list(self) -> None:
        sll = SinglyLinkedList()
        sll.append(1)
        sll.append(2)
        sll.prepend(0)
        self.assertEqual(sll.to_list(), [0, 1, 2])

        self.assertTrue(sll.delete(1))
        self.assertEqual(sll.to_list(), [0, 2])

        sll.reverse()
        self.assertEqual(sll.to_list(), [2, 0])

    def test_doubly_linked_list(self) -> None:
        dll = DoublyLinkedList()
        dll.push_back(10)
        dll.push_front(5)
        dll.push_back(20)
        self.assertEqual(dll.to_list(), [5, 10, 20])

        self.assertEqual(dll.pop_front(), 5)
        self.assertEqual(dll.pop_back(), 20)
        self.assertEqual(dll.to_list(), [10])

    def test_floyd_cycle_detection(self) -> None:
        n1 = SinglyNode(1)
        n2 = SinglyNode(2)
        n3 = SinglyNode(3)
        n1.next = n2
        n2.next = n3
        self.assertFalse(detect_cycle_floyd(n1))

        n3.next = n1  # Cycle
        self.assertTrue(detect_cycle_floyd(n1))

    def test_merge_two_sorted_lists(self) -> None:
        l1 = SinglyNode(1, SinglyNode(3, SinglyNode(5)))
        l2 = SinglyNode(2, SinglyNode(4, SinglyNode(6)))
        merged = merge_two_sorted_lists(l1, l2)

        res = []
        curr = merged
        while curr:
            res.append(curr.value)
            curr = curr.next
        self.assertEqual(res, [1, 2, 3, 4, 5, 6])


class TestStackAndQueue(unittest.TestCase):
    def test_stack_and_min_stack(self) -> None:
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(len(stack), 1)

        min_stack = MinStack()
        min_stack.push(5)
        min_stack.push(2)
        min_stack.push(10)
        min_stack.push(1)
        self.assertEqual(min_stack.get_min(), 1)
        min_stack.pop()
        self.assertEqual(min_stack.get_min(), 2)

    def test_monotonic_stack_and_valid_parentheses(self) -> None:
        self.assertEqual(next_greater_element([4, 5, 2, 25]), [5, 25, 25, -1])
        self.assertTrue(is_valid_parentheses("{[()]}"))
        self.assertFalse(is_valid_parentheses("{[(]}"))

    def test_queues(self) -> None:
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 1)

        cq = CircularQueue(3)
        self.assertTrue(cq.enqueue(10))
        self.assertTrue(cq.enqueue(20))
        self.assertTrue(cq.enqueue(30))
        self.assertFalse(cq.enqueue(40))
        self.assertEqual(cq.dequeue(), 10)
        self.assertTrue(cq.enqueue(40))

        pq = PriorityQueue()
        pq.push("task3", priority=3)
        pq.push("task1", priority=1)
        pq.push("task2", priority=2)
        self.assertEqual(pq.pop(), "task1")
        self.assertEqual(pq.pop(), "task2")


class TestHashTable(unittest.TestCase):
    def test_hash_table_crud(self) -> None:
        ht = HashTable(initial_capacity=4)
        ht.put("a", 1)
        ht.put("b", 2)
        ht["c"] = 3
        ht["d"] = 4  # Triggers resize

        self.assertEqual(ht.get("a"), 1)
        self.assertEqual(ht["b"], 2)
        self.assertEqual(len(ht), 4)

        self.assertTrue(ht.contains("c"))
        del ht["c"]
        self.assertFalse(ht.contains("c"))

        with self.assertRaises(KeyError):
            _ = ht["nonexistent"]


class TestTreesAndBST(unittest.TestCase):
    def test_binary_tree_traversals(self) -> None:
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(3)
        root.left.left = BinaryTreeNode(4)
        bt = BinaryTree(root)

        self.assertEqual(bt.preorder_traversal(), [1, 2, 4, 3])
        self.assertEqual(bt.inorder_traversal(), [4, 2, 1, 3])
        self.assertEqual(bt.postorder_traversal(), [4, 2, 3, 1])
        self.assertEqual(bt.level_order_traversal(), [[1], [2, 3], [4]])
        self.assertEqual(bt.height(), 2)

    def test_bst_operations(self) -> None:
        bst = BinarySearchTree()
        for x in [10, 5, 15, 3, 7, 12, 18]:
            bst.insert(x)

        self.assertTrue(bst.search(7))
        self.assertFalse(bst.search(20))
        self.assertEqual(bst.inorder(), [3, 5, 7, 10, 12, 15, 18])
        self.assertEqual(bst.find_min(), 3)
        self.assertEqual(bst.find_max(), 18)

        self.assertEqual(bst.lowest_common_ancestor(3, 7), 5)

        bst.delete(5)
        self.assertEqual(bst.inorder(), [3, 7, 10, 12, 15, 18])


class TestHeapTrieGraph(unittest.TestCase):
    def test_heaps(self) -> None:
        min_h = MinHeap([5, 3, 8, 1, 2])
        self.assertEqual(min_h.extract_min(), 1)
        self.assertEqual(min_h.extract_min(), 2)

        max_h = MaxHeap([5, 3, 8, 1, 2])
        self.assertEqual(max_h.extract_max(), 8)
        self.assertEqual(max_h.extract_max(), 5)

    def test_trie(self) -> None:
        trie = Trie()
        trie.insert("apple")
        trie.insert("app")

        self.assertTrue(trie.search("apple"))
        self.assertTrue(trie.search("app"))
        self.assertFalse(trie.search("appl"))
        self.assertTrue(trie.starts_with("appl"))

        trie.delete("app")
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.search("apple"))

    def test_graph_algorithms(self) -> None:
        # Undirected graph for BFS, DFS, Dijkstra
        g = Graph(directed=False)
        g.add_edge("A", "B", 1)
        g.add_edge("A", "C", 4)
        g.add_edge("B", "C", 2)
        g.add_edge("B", "D", 5)
        g.add_edge("C", "D", 1)

        self.assertEqual(bfs(g, "A"), ["A", "B", "C", "D"])
        self.assertEqual(dfs(g, "A"), ["A", "B", "C", "D"])

        dist = dijkstra(g, "A")
        self.assertEqual(dist["D"], 4.0)  # A -> B (1) -> C (2) -> D (1) = 4

        # Directed DAG for Topological Sort
        dag = Graph(directed=True)
        dag.add_edge("5", "11")
        dag.add_edge("7", "11")
        dag.add_edge("7", "8")
        dag.add_edge("3", "8")
        dag.add_edge("11", "2")
        dag.add_edge("11", "9")
        dag.add_edge("8", "9")

        topo = topological_sort(dag)
        self.assertEqual(len(topo), 7)
        self.assertLess(topo.index("5"), topo.index("11"))

        # Disjoint Set
        dsu = DisjointSet(["A", "B", "C", "D"])
        self.assertTrue(dsu.union("A", "B"))
        self.assertTrue(dsu.union("C", "D"))
        self.assertFalse(dsu.union("A", "B"))
        self.assertTrue(dsu.union("B", "C"))
        self.assertEqual(dsu.find("A"), dsu.find("D"))


if __name__ == "__main__":
    unittest.main()
