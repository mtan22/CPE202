from typing import List, Any, Optional

class HashTable:

    def __init__(self, table_size: int):            # can add additional attributes
        self.table_size = table_size                # initial table size
        self.hash_table: List = [None]*table_size   # hash table
        self.num_items = 0                          # empty hash table

    def insert(self, key: str, value: Any) -> None:
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        When used with the concordance, value is a Python List of line numbers.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        i = 0
        index = self.horner_hash(key)
        factor = i ** 2
        if self.hash_table[index] is None:
            self.num_items += 1
            self.hash_table[index + factor] = (key, [value])
        else:
            m = 0
            while key != self.hash_table[index + (i ** 2) - m][0]:
                i += 1
                if self.table_size <= index + (i ** 2) - m:
                    m = m + self.table_size
                if self.hash_table[index + (i ** 2) - m] is not None:
                    continue
                self.num_items += 1
                self.hash_table[index + (i ** 2) - m] = (key, [value])
                break
            if self.hash_table[index + (i ** 2) - m][0] == key and value not in self.hash_table[index + (i ** 2) - m][1]:
                self.hash_table[index + (i ** 2) - m][1].append(value)
        if 0.5 < self.get_load_factor():
            self.rehash_helper()

    def horner_hash(self, key: str) -> int:
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        horner = 0
        index = 0
        while (min(8, len(key))) > index:
            horner = horner + ord(key[index]) * (31 ** (min(8, len(key)) - 1 - index))
            index = index + 1
        num = horner % self.table_size
        return num

    def in_table(self, key: str) -> bool:
        """ Returns True if key is in an entry of the hash table, False otherwise. Must be O(1)."""
        if self.get_index(key) is not None:
            return True
        return False

    def get_index(self, key: str) -> Optional[int]:
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None. Must be O(1)."""
        i = 0
        m = 0
        while self.hash_table[self.horner_hash(key) + (i ** 2) - m] is not None:
            if self.hash_table[self.horner_hash(key) + (i ** 2) - m][0] != key:
                i = i + 1
                if self.table_size <= self.horner_hash(key) + (i ** 2) - m:
                    m = m + self.table_size
                continue
            return self.horner_hash(key) + (i ** 2) - m
        return None

    def get_all_keys(self) -> List:
        """ Returns a Python list of all keys in the hash table."""
        key_list = []
        for i in self.hash_table:
            if i is not None:
                key_list.append(i[0])
        return key_list

    def get_value(self, key: str) -> Any:
        """ Returns the value (for concordance, list of line numbers) associated with the key.
        If key is not in hash table, returns None. Must be O(1)."""
        if self.get_index(key) is None:
            return None
        return self.hash_table[self.get_index(key)][1]

    def get_num_items(self) -> int:
        """ Returns the number of entries (words) in the table. Must be O(1)."""
        return self.num_items

    def get_table_size(self) -> int:
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self) -> float:
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.get_num_items() / self.table_size

    def rehash_helper(self) -> None:
        diff: List[Any] = []
        for i in self.hash_table:
            if i is not None:
                diff = diff + [i]
        self.num_items = 0
        self.table_size = self.table_size * 2 + 1
        self.hash_table = self.table_size * [None]
        for i in diff:
            j = 0
            m = 0
            if self.hash_table[self.horner_hash(i[0])] is None:
                tuple = (i[0], i[1])
                self.hash_table[self.horner_hash(i[0]) + (j ** 2)] = tuple
                self.num_items += 1
            while self.hash_table[self.horner_hash(i[0]) + (j ** 2) - m][0] != i[0]:
                j = j + 1
                tuple = (i[0], i[1])
                if self.hash_table[self.horner_hash(i[0]) + (j ** 2) - m] is None:
                    self.hash_table[self.horner_hash(i[0]) + (j ** 2) - m] = tuple

