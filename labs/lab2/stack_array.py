# Lab 2: Michelle Tan
# Instructor: Prof. Parkinson

from typing import Optional, List, Any


# Stack class implemented with array
class Stack:
    """Implements an efficient last-in first-out Abstract Data Type using a Python List"""

    # capacity is max number of Nodes, init_items is optional List parameter for initialization
    # if the length of the init_items List exceeds capacity, raise IndexError
    def __init__(self, capacity: int, init_items: Optional[List] = None):
        """Creates an empty stack with a capacity"""
        self.capacity = capacity  # capacity of stack
        self.items = [None] * capacity  # array for stack
        self.num_items = 0  # number of items in stack
        if init_items is not None:  # if init_items is not None, initialize stack
            if len(init_items) > capacity:
                raise IndexError
            else:
                self.num_items = len(init_items)
                self.items[:self.num_items] = init_items

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Stack):
            return (self.capacity == other.capacity
                    and self.items[:self.num_items] == other.items[:other.num_items])
        else:
            return False

    def __repr__(self) -> str:
        return ("Stack({!r}, {!r})".format(self.capacity, self.items[:self.num_items]))

    def is_empty(self) -> bool:
        if self.num_items == 0:
            return True
        else:
            return False

    def is_full(self) -> bool:
        if self.num_items == self.capacity:
            return True
        else:
            return False

    def push(self, item: Any) -> Any:
        self.items[self.num_items] = item
        self.num_items += 1

    def pop(self) -> Any:
        if self.num_items == 0:
            raise IndexError
        else:
            self.num_items -= 1
            pop_item = self.items[self.num_items]
            return pop_item

    def peek(self) -> Any:
        if self.capacity == 0 or self.num_items == 0:
            raise IndexError
        else:
            return self.items[self.num_items - 1]

    def size(self) -> int:
        return self.num_items
