from typing import Any, Tuple, List


class MyHashTable:

    def __init__(self, table_size: int = 11):
        self.table_size = table_size
        self.hash_table: List = [[] for _ in range(table_size)] # List of lists implementation
        self.num_items = 0
        self.num_collisions = 0

    def insert(self, key: int, value: Any) -> None:
        """Takes a key, and an item.  Keys are valid Python non-negative integers.
        If key is negative, raise ValueError exception
        The function will insert the key-item pair into the hash table based on the
        hash value of the key mod the table size (hash_value = key % table_size)"""
        if key < 0:
            raise ValueError
        hash_value = key % self.table_size
        bool = False
        vals = self.hash_table[hash_value]
        size = self.table_size
        lista: List = []
        for i in vals:
            if i[0] == key:
                bool = True
        if bool is False:
            tuple = (key, value)
            vals.append(tuple)
            if 1 < len(self.hash_table[hash_value]):
                self.num_collisions += 1
            self.num_items += 1


    def get_item(self, key: int) -> Any:
        """Takes a key and returns the item from the hash table associated with the key.
        If no key-item pair is associated with the key, the function raises a LookupError exception."""
        hash_value = key % self.table_size
        vals = self.hash_table[hash_value]
        if self.hash_table[hash_value] is None or not self.hash_table[hash_value]:
            raise LookupError
        for i in vals:
            if i[0] == key:
                return i[1]
        raise LookupError

    def remove(self, key: int) -> Tuple[int, Any]:
        """Takes a key, removes the key-item pair from the hash table and returns the key-item pair.
        If no key-item pair is associated with the key, the function raises a LookupError exception.
        (The key-item pair should be returned as a tuple)"""
        hash_value = key % self.table_size
        vals = self.hash_table[hash_value]
        for i in vals:
            if i[0] == key:
                val = i
                vals.remove(i)
                self.num_items -= 1
                return val
        else:
            raise LookupError


    def load_factor(self) -> float:
        """Returns the current load factor of the hash table"""
        return self.num_items / self.table_size

    def size(self) -> int:
        """Returns the number of key-item pairs currently stored in the hash table"""
        return self.num_items

    def collisions(self) -> int:
        """Returns the number of collisions that have occurred during insertions into the hash table"""
        return self.num_collisions
