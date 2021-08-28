# Name: Michelle Tan
# Project 3: Huffman Tree
# Instructor: Prof. Turner

from __future__ import annotations
from typing import List, Optional


class HuffmanNode:
    def __init__(self, char_ascii: int, freq: int, left: Optional[HuffmanNode] = None,
                 right: Optional[HuffmanNode] = None):
        self.char_ascii = char_ascii  # stored as an integer - the ASCII character code value
        self.freq = freq  # the frequency associated with the node
        self.left = left  # Huffman tree (node) to the left!
        self.right = right  # Huffman tree (node) to the right

    def __lt__(self, other: HuffmanNode) -> bool:
        return comes_before(self, other)


def comes_before(a: HuffmanNode, b: HuffmanNode) -> bool:
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq != b.freq:
        return a.freq < b.freq
    else:
        return a.char_ascii < b.char_ascii


def combine(a: HuffmanNode, b: HuffmanNode) -> HuffmanNode:
    """Creates a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lower of the a and b char ASCII values"""
    if a.char_ascii >= b.char_ascii:
        c_value = b.char_ascii
    else:
        c_value = a.char_ascii
    if not comes_before(a, b):
        add_freq = a.freq + b.freq
        new_node = HuffmanNode(c_value, add_freq)
        new_node.right = a
        new_node.left = b
    else:
        add_freq = a.freq + b.freq
        new_node = HuffmanNode(c_value, add_freq)
        new_node.left = a
        new_node.right = b
    return new_node


def cnt_freq(filename: str) -> List:
    """Opens a text file with a given file name (passed as a string) and counts the
    frequency of occurrences of all the characters within that file
    Returns a Python List with 256 entries - counts are initialized to zero.
    The ASCII value of the characters are used to index into this list for the frequency counts"""
    entries = [0] * 256
    file = open(filename, "r")
    for index in file:
        for j in index:
            char_ascii = ord(j)
            entries[char_ascii] = entries[char_ascii] + 1
    file.close()
    return entries


def create_huff_tree(char_freq: List) -> Optional[HuffmanNode]:
    """Input is the list of frequencies (provided by cnt_freq()).
    Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree. Returns None if all counts are zero."""
    huffman_tree = []
    for index in range(len(char_freq)):
        if char_freq[index] == 0:
            continue
        huffman_tree.append(HuffmanNode(index, char_freq[index]))
    huffman_tree.sort()
    while 1 < len(huffman_tree):
        first = huffman_tree[0]
        second = huffman_tree[1]
        node = combine(first, second)
        huffman_tree = huffman_tree[2:]
        huffman_tree.append(node)
        huffman_tree.sort()
    return huffman_tree[0]


def create_code_helper(node: Optional[HuffmanNode], array: List, code: str = "") -> None:
    if node is not None:
        if (node.right and node.left) is None:
            array[node.char_ascii] = code
        else:
            if node.right is not None:
                right_side = code + "1"
                create_code_helper(node.right, array, right_side)
            if node.left is not None:
                left_side = code + "0"
                create_code_helper(node.left, array, left_side)


def create_code(node: Optional[HuffmanNode]) -> List:
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the array, with the resulting Huffman code for that character stored at that location.
    Characters that are unused should have an empty string at that location"""
    code_array = [""] * 256
    create_code_helper(node, code_array)
    return code_array


def create_header(freqs: List) -> str:
    """Input is the list of frequencies (provided by cnt_freq()).
    Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    header_str = ""
    for index in range(len(freqs)):
        if freqs[index] == 0:
            continue
        i_str = str(index)
        freq_str = str(freqs[index])
        space = " "
        header_str += i_str + space + freq_str + space
    final_header = header_str.rstrip()
    return final_header


def huffman_encode(in_file: str, out_file: str) -> None:
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    empty = ""
    try:
        file = open(in_file, "r")
        file.close()
    except:
        raise OSError
    freq = cnt_freq(in_file)
    text = huffman_encoder_helper(freq, in_file)
    out_text = open(out_file, "w")
    out_text.write(create_header(freq))
    if text != empty:
        out_text.write("\n")
        out_text.write(text)
    out_text.close()


def huffman_encoder_helper(freq: List, filename: str) -> str:
    placehold = ""
    text = ""
    file = open(filename, "r")
    for i in file:
        placehold += i
    file.close()
    huff_node = create_huff_tree(freq)
    code_values = create_code(huff_node)
    for j in list(placehold):
        ascii_num = ord(j)
        text += code_values[ascii_num]
    return text


def huffman_decode(encoded_file: str, decode_file: str) -> None:
    """Reads an encoded text file, and writes the decoded text into an output
    text file, using the Huffman Tree produced by using the header information."""
    placeholder = ''
    try:
        encode = open(encoded_file, "r")
    except:
        raise FileNotFoundError
    header = encode.readline()
    d_file = open(decode_file, "w")
    if 0 < len(header):
        placeholder = ''
        freq = parse_header(header)
        huff_node = create_huff_tree(freq)
        text = list(encode.readline())
        first = huff_node
        encode.close()
        current = huff_node
        length = len(text)
        if length != 0:
            for i in range(len(text)):
                if current is not None:
                    if text[i] == "0" and current.left is not None:
                        current = current.left
                    elif text[i] == '1' and current.right is not None:
                        current = current.right
                    if current.left is None and current.right is None:
                        placeholder = placeholder + chr(current.char_ascii)
                        current = first
        else: # coverage error, i tested an empty file so i'm unsure why
            for i in range(len(freq)):
                if not freq[i] == 0:
                    placeholder = freq[i] * chr(i)

    d_file.write(placeholder)
    d_file.close()
    encode.close()

def parse_header(header_string: str) -> List:
    """takes a string input parameter and returns a list of frequencies."""
    freq = [0] * 256
    header = header_string.split(" ")
    for i in range(0, len(header), +2):
        freq[int(header[i])] = int(header[i + 1])
    return freq