"""
Binary Tree Implementation and Traversals.

Time Complexities:
- Traversals (Pre/In/Post/Level Order): O(n) time, O(h) space where h is tree height
- Height & Node Count: O(n)
"""

from collections import deque
from typing import Any, List, Optional


class BinaryTreeNode:
    def __init__(
        self,
        value: Any,
        left: Optional["BinaryTreeNode"] = None,
        right: Optional["BinaryTreeNode"] = None,
    ) -> None:
        self.value: Any = value
        self.left: Optional["BinaryTreeNode"] = left
        self.right: Optional["BinaryTreeNode"] = right


class BinaryTree:
    """General Binary Tree structure."""

    def __init__(self, root: Optional[BinaryTreeNode] = None) -> None:
        self.root: Optional[BinaryTreeNode] = root

    def preorder_traversal(self) -> List[Any]:
        """Root -> Left -> Right"""
        result: List[Any] = []

        def _traverse(node: Optional[BinaryTreeNode]) -> None:
            if node:
                result.append(node.value)
                _traverse(node.left)
                _traverse(node.right)

        _traverse(self.root)
        return result

    def inorder_traversal(self) -> List[Any]:
        """Left -> Root -> Right"""
        result: List[Any] = []

        def _traverse(node: Optional[BinaryTreeNode]) -> None:
            if node:
                _traverse(node.left)
                result.append(node.value)
                _traverse(node.right)

        _traverse(self.root)
        return result

    def postorder_traversal(self) -> List[Any]:
        """Left -> Right -> Root"""
        result: List[Any] = []

        def _traverse(node: Optional[BinaryTreeNode]) -> None:
            if node:
                _traverse(node.left)
                _traverse(node.right)
                result.append(node.value)

        _traverse(self.root)
        return result

    def level_order_traversal(self) -> List[List[Any]]:
        """BFS Level order traversal returning list of levels."""
        if not self.root:
            return []

        levels: List[List[Any]] = []
        queue: deque = deque([self.root])

        while queue:
            level_size = len(queue)
            current_level: List[Any] = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(current_level)

        return levels

    def height(self) -> int:
        """Returns height of tree (number of edges on longest root-to-leaf path)."""

        def _get_height(node: Optional[BinaryTreeNode]) -> int:
            if not node:
                return -1
            return 1 + max(_get_height(node.left), _get_height(node.right))

        return _get_height(self.root)

    def count_nodes(self) -> int:
        def _count(node: Optional[BinaryTreeNode]) -> int:
            if not node:
                return 0
            return 1 + _count(node.left) + _count(node.right)

        return _count(self.root)
