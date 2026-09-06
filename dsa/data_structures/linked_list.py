"""
Singly and Doubly Linked List Implementations.

Time Complexities:
- Insert Head / Push Front: O(1)
- Insert Tail / Push Back: O(1) with tail pointer
- Delete Head / Pop Front: O(1)
- Search / Delete by Value: O(n)
- Reverse List: O(n) time, O(1) space
- Floyd's Cycle Detection: O(n) time, O(1) space
- Merge Two Sorted Lists: O(n + m) time, O(1) auxiliary space
"""

from typing import Any, List, Optional


class SinglyNode:
    def __init__(self, value: Any, next_node: Optional["SinglyNode"] = None) -> None:
        self.value: Any = value
        self.next: Optional["SinglyNode"] = next_node


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[SinglyNode] = None
        self.tail: Optional[SinglyNode] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def append(self, value: Any) -> None:
        """Appends node to end of list O(1)."""
        new_node = SinglyNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value: Any) -> None:
        """Prepends node to front of list O(1)."""
        new_node = SinglyNode(value, self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def delete(self, value: Any) -> bool:
        """Deletes first occurrence of value. Returns True if deleted."""
        current = self.head
        prev: Optional[SinglyNode] = None

        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next

                if current == self.tail:
                    self.tail = prev

                self._size -= 1
                return True
            prev = current
            current = current.next
        return False

    def reverse(self) -> None:
        """Reverses the linked list in-place in O(n) time and O(1) space."""
        prev: Optional[SinglyNode] = None
        current = self.head
        self.tail = self.head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        self.head = prev

    def to_list(self) -> List[Any]:
        """Converts linked list to Python list."""
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result


class DoublyNode:
    def __init__(
        self,
        value: Any,
        prev_node: Optional["DoublyNode"] = None,
        next_node: Optional["DoublyNode"] = None,
    ) -> None:
        self.value: Any = value
        self.prev: Optional["DoublyNode"] = prev_node
        self.next: Optional["DoublyNode"] = next_node


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[DoublyNode] = None
        self.tail: Optional[DoublyNode] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def push_front(self, value: Any) -> None:
        """Adds value to front O(1)."""
        new_node = DoublyNode(value, prev_node=None, next_node=self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self._size += 1

    def push_back(self, value: Any) -> None:
        """Adds value to back O(1)."""
        new_node = DoublyNode(value, prev_node=self.tail, next_node=None)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self._size += 1

    def pop_front(self) -> Any:
        """Removes and returns front element O(1)."""
        if not self.head:
            raise IndexError("Pop from empty DoublyLinkedList.")
        val = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return val

    def pop_back(self) -> Any:
        """Removes and returns back element O(1)."""
        if not self.tail:
            raise IndexError("Pop from empty DoublyLinkedList.")
        val = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return val

    def to_list(self) -> List[Any]:
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result


def detect_cycle_floyd(head: Optional[SinglyNode]) -> bool:
    """
    Detects cycle in singly linked list using Floyd's Tortoise and Hare algorithm.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def merge_two_sorted_lists(
    l1: Optional[SinglyNode], l2: Optional[SinglyNode]
) -> Optional[SinglyNode]:
    """
    Merges two sorted singly linked lists into one sorted linked list.

    Time Complexity: O(n + m)
    Space Complexity: O(1) auxiliary
    """
    dummy = SinglyNode(0)
    tail = dummy

    while l1 and l2:
        if l1.value <= l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next
