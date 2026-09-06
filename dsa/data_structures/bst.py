"""
Binary Search Tree (BST) Implementation.

Time Complexities:
- Insert: O(h) average O(log n), worst-case O(n)
- Search: O(h) average O(log n), worst-case O(n)
- Delete: O(h) average O(log n), worst-case O(n)
- Lowest Common Ancestor (LCA): O(h)
Where h is height of tree.
"""

from typing import Any, List, Optional


class BSTNode:
    def __init__(
        self,
        value: Any,
        left: Optional["BSTNode"] = None,
        right: Optional["BSTNode"] = None,
    ) -> None:
        self.value: Any = value
        self.left: Optional["BSTNode"] = left
        self.right: Optional["BSTNode"] = right


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[BSTNode] = None

    def insert(self, value: Any) -> None:
        def _insert(node: Optional[BSTNode], val: Any) -> BSTNode:
            if not node:
                return BSTNode(val)
            if val < node.value:
                node.left = _insert(node.left, val)
            elif val > node.value:
                node.right = _insert(node.right, val)
            return node

        self.root = _insert(self.root, value)

    def search(self, value: Any) -> bool:
        curr = self.root
        while curr:
            if curr.value == value:
                return True
            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def find_min(self) -> Optional[Any]:
        if not self.root:
            return None
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.value

    def find_max(self) -> Optional[Any]:
        if not self.root:
            return None
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.value

    def delete(self, value: Any) -> None:
        def _min_node(node: BSTNode) -> BSTNode:
            curr = node
            while curr.left:
                curr = curr.left
            return curr

        def _delete(node: Optional[BSTNode], val: Any) -> Optional[BSTNode]:
            if not node:
                return None
            if val < node.value:
                node.left = _delete(node.left, val)
            elif val > node.value:
                node.right = _delete(node.right, val)
            else:
                # Node to delete found
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left

                # Node with two children: get inorder successor (smallest in right subtree)
                temp = _min_node(node.right)
                node.value = temp.value
                node.right = _delete(node.right, temp.value)

            return node

        self.root = _delete(self.root, value)

    def inorder(self) -> List[Any]:
        result: List[Any] = []

        def _inorder(node: Optional[BSTNode]) -> None:
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)

        _inorder(self.root)
        return result

    def lowest_common_ancestor(self, p: Any, q: Any) -> Optional[Any]:
        """Finds lowest common ancestor of values p and q in BST."""
        curr = self.root
        while curr:
            if p < curr.value and q < curr.value:
                curr = curr.left
            elif p > curr.value and q > curr.value:
                curr = curr.right
            else:
                # Splitting point found or matched node
                return curr.value
        return None
