from typing import Any, List

class MinHeap:

    def __init__(self, capacity: int = 50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.heap: List = [None]*(capacity+1)     # index 0 not used for heap
        self.num_items = 0                  # empty heap

    def enqueue(self, item: Any) -> None:
        """inserts "item" into the heap
        Raises IndexError if there is no room in the heap"""
        if self.is_full():
            raise IndexError
        else:
            self.heap[self.num_items + 1] = item
            self.num_items += 1
            self.perc_up(self.num_items)

    def peek(self) -> Any:
        """returns root of heap (highest priority) without changing the heap
        Raises IndexError if the heap is empty"""
        if self.is_empty():
            raise IndexError
        else:
            return self.heap[1]

    def dequeue(self) -> Any:
        """returns item at root (highest priority) - removes it from the heap and restores the heap property
           Raises IndexError if the heap is empty"""
        if self.is_empty():
            raise IndexError
        else:
            item = self.heap[1]
            self.heap[1] = self.heap[self.num_items]
            self.perc_down(1)
            self.num_items -= 1
            return item

    def contents(self) -> List:
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)
        If heap is empty, returns empty list []"""
        if self.is_empty():
            return []
        return self.heap[1: self.num_items + 1]

    def build_heap(self, alist: List) -> None:
        """Discards the items in the current heap and builds a heap from
        the items in alist using the bottom up method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""
        i = len(alist) // 2
        self.num_items = len(alist)
        for i in range(len(alist)):
            self.heap[i+1] = alist[i]
        while (i > 0):
            self.perc_down(i)
            i = i - 1

    def is_empty(self) -> bool:
        """returns True if the heap is empty, false otherwise"""
        if self.num_items == 0:
            return True
        else:
            return False

    def is_full(self) -> bool:
        """returns True if the heap is full, false otherwise"""
        capacity = self.capacity()
        if self.num_items == capacity:
            return True
        else:
            return False

    def capacity(self) -> int:
        """This is the maximum number of a entries the heap can hold, which is
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return (len(self.heap) - 1)
    
    def size(self) -> int:
        """the actual number of elements in the heap, not the capacity"""
        return self.num_items

    def perc_down(self,i: int) -> None:
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while (i * 2) <= self.num_items:
            mc = self.minimumchild(i)
            if self.heap[i] > self.heap[mc]:
                temp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = temp
            i = mc

    def minimumchild(self, i: int) -> int:
        if i * 2 + 1 > self.num_items:
            return i * 2
        else:
            if self.heap[i * 2] < self.heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def perc_up(self, i: int) -> None:
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while (i//2) > 0:
            if self.heap[i] < self.heap[i//2]:
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i = (i//2)

    def heap_sort_ascending(self, alist: List) -> None:
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate alist to put the items in ascending order"""
        n = len(alist)
        for i in range(n // 2 - 1, -1, -1):
            self.heap_sort_helper(alist, n, i)
        for i in range(n - 1, 0, -1):
            alist[i], alist[0] = alist[0], alist[i]
            self.heap_sort_helper(alist, i, 0)

    def heap_sort_helper(self, lista: List, n: int, i: int) -> None:
        maximum = i
        m = 2 * i + 1
        p = 2 * i + 2
        if m < n and lista[maximum] < lista[m]:
            maximum = m
        if p < n and lista[maximum] < lista[p]:
            maximum = p
        if maximum != i:
            lista[i], lista[maximum] = lista[maximum], lista[i]
            self.heap_sort_helper(lista, n, maximum)
