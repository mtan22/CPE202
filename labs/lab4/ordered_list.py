//REMOVE THIS

from __future__ import annotations
from typing import Optional, Any, List

class Node:
    """Node for use with doubly-linked list"""
    def __init__(self, item: Any):
        self.item = item  # item held by Node
        self.next: Node = self  # reference to next Node, init to this Node
        self.prev: Node = self  # reference to previous Node, init to this Node

class OrderedList:
    """A doubly-linked ordered list of integers, 
    from lowest (head of list, sentinel.next) to highest (tail of list, sentinel.prev)"""
    def __init__(self) -> None:
        """Use only a sentinel Node. No other instance variables"""
        self.sentinel: Node = Node(None)    # Empty linked list, just sentinel Node
        self.sentinel.next = self.sentinel  # Initialize next to sentinel
        self.sentinel.prev = self.sentinel  # Initialize prev to sentinel

    def __eq__(self, other: object) -> bool:
        lists_equal = True
        if not isinstance(other, OrderedList):
            lists_equal = False
        else:
            s_cur = self.sentinel.next
            o_cur = other.sentinel.next
            while s_cur != self.sentinel and o_cur != other.sentinel:
                if s_cur.item != o_cur.item:
                    lists_equal = False
                s_cur = s_cur.next
                o_cur = o_cur.next
            if s_cur != self.sentinel or o_cur != other.sentinel:
                lists_equal = False
        return lists_equal

    def is_empty(self) -> bool:
        """Returns back True if OrderedList is empty"""
        # This function runs correctly
        if self.sentinel.next.item is None:
            return True
        else:
            return False

    def add(self, item: Any) -> None:
        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list)
        If item is already in list, do not add again (no duplicate items)"""
        # This function runs correctly
        current = self.sentinel.next
        prev = None
        while current != self.sentinel or current.item is not None and current.item < item:
            current = current.next
        new = Node(item)
        new.next = current
        current.prev.next = new
        current.prev = new
        new.prev = current.prev


    def remove(self, item: Any) -> bool:
        """Removes an item from OrderedList. If item is removed (was in the list) returns True
        If item was not removed (was not in the list) returns False"""
        # I think this function runs correctly, I might be wrong
        count = 0
        current = self.sentinel.next
        while current != self.sentinel:
            if item == current.item:
                current = current.prev
                return True
            else:
                count += 1
                current = current.next
        return False

    def index(self, item: Any) -> Optional[int]:
        """Returns index of an item in OrderedList (assuming head of list is index 0).
        If item is not in list, return None"""
        # This function runs correctly
        count = 0
        current = self.sentinel.next
        while current != self.sentinel:
            if item == current.item:
                return count
            else:
                count += 1
                current = current.next
        return None

    def pop(self, index: int) -> Any:
        """Removes and returns item at index (assuming head of list is index 0).
        If index is negative or >= size of list, raises IndexError"""
        # I think this function runs correctly, I might be wrong
        count = 0
        current = self.sentinel.next
        while current != self.sentinel:
            if index == count:
                current = current.prev
                self.sentinel = current
                return current.item
            else:
                count += 1
        if index < 0 or index >= count:
            raise IndexError

    def search(self, item: Any) -> bool:
        """Searches OrderedList for item, returns True if item is in list, False otherwise - USE RECURSION"""
        # This function does not run correctly
        current = self.sentinel.next
        if current != self.sentinel:
            if item == current.item:
                return True
            else:
                current = self.search(item)
        return False

    def python_list(self) -> List:
        """Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""
        # This function runs correctly
        py_list = []
        current = self.sentinel.next
        while current != self.sentinel:
            py_list.append(current.item)
            current = current.next
        return py_list

    def python_list_reversed(self) -> List:
        # This function does not run correctly
        """Return a Python list representation of OrderedList, from tail to head, USING RECURSION
        For example, list with integers 1, 2, and 3 would return [3, 2, 1]"""
        py_list = []
        if self.sentinel is None:
            return py_list
        return self.py_list_reversed_helper(self.sentinel, py_list)

    def py_list_reversed_helper(self, current, py_list: List) -> List:
        # This function does not run correctly
        if current != self.sentinel.prev:
            current = self.sentinel.prev
            py_list.append(current)
            return self.py_list_reversed_helper(self.sentinel.prev, py_list)
        else:
            return py_list


    def size(self) -> int:
        # This function runs correctly
        """Returns number of items in the OrderedList - USE RECURSION"""
        return len(self.python_list())
