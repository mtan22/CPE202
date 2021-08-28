from typing import Any, List, Optional
from hash_quad import *
import string

class Concordance:

    def __init__(self) -> None:
        """ Starting size of hash table should be 191: self.concordance_table = HashTable(191) """
        self.stop_table: Optional[HashTable] = None          # hash table for stop words
        self.concordance_table: HashTable = HashTable(191)              # hash table for concordance

    def load_stop_table(self, filename: str) -> None:
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.stop_table = HashTable(191)
        try:
            input_file = open(filename)
            for i in input_file:
                self.stop_table.insert(i.rstrip(), 0)
        except FileNotFoundError:
            raise FileNotFoundError('File does not exist')
        input_file.close()

    def load_concordance_table(self, filename: str) -> None:
        """ Read words from input text file (filename) and insert them into the concordance hash table,
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)

        Process of adding new line numbers for a word (key) in the concordance:
            If word is in table, get current value (list of line numbers), append new line number, insert (key, value)
            If word is not in table, insert (key, value), where value is a Python List with the line number
        If file does not exist, raise FileNotFoundError """
        line_num = 1
        try:
            input_file = open(filename)
        except FileNotFoundError:
            raise FileNotFoundError('File does not exist')
        for i in input_file:
            empty_str = ''
            for j in i:
                if j == ' ':
                    empty_str += ' '
                elif j == "'":
                    empty_str += ''
                elif j in string.punctuation:
                    empty_str += ' '
                elif j in string.ascii_uppercase:
                    char = chr(ord(j) + 32)
                    empty_str += char
                elif j in string.ascii_lowercase:
                    empty_str += j
            for m in empty_str.split():
                if not self.stop_table.in_table(m):
                    self.concordance_table.insert(m, line_num)
            line_num += 1
        input_file.close()

    def write_concordance(self, filename: str) -> None:
        """ Write the concordance entries to the output file(filename)
        See sample output files for format. """
        entries = []
        output_file = open(filename, 'w')
        for i in self.concordance_table.hash_table:
            if i is None:
                continue
            lnum = ''
            for j in i[1]:
                str_num = str(j)
                lnum = lnum + ' ' + str_num
            entries.append(str(i[0]) + ':' + lnum)
        entries.sort()
        if len(entries) != 0:
            slice = entries[:-1]
            for i in slice:
                output_file.write(i)
                output_file.write('\n')
            output_file.write(entries[-1])
            output_file.close()
