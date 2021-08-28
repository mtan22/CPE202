# Project 1 - rec_list.py: Michelle Tan
# Instructor: Prof. Parkinson

from __future__ import annotations
from typing import Optional
from typing import Any
from typing import Tuple


# NodeList is
# None or
# Node(value, rest), where rest is the rest of the NodeList
class Node:
    def __init__(self, value: Any, rest: Optional[Node]):
        self.value = value
        self.rest = rest

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return (self.value == other.value
                    and self.rest == other.rest
                    )
        else:
            return False # pragma no cover

    def __repr__(self) -> str:
        return "Node({!r}, {!r})".format(self.value, self.rest) #pragma no cover


# a StrList is one of
# - None, or
# - Node(string, StrList)

# StrList -> string
# Returns first (as determined by Python compare) string in StrList
# If StrList is empty (None), return None
# Must be implemented recursively
def first_string(strlist: Optional[Node]) -> Optional[str]:
    if strlist is None:
        return None
    elif strlist.rest is None:
        return strlist.value
    else:
        first = first_string(strlist.rest)
        first = min(strlist.value, first)
        return first


# StrList -> (StrList, StrList, StrList)
# Returns a tuple with 3 new StrLists,
# the first one with strings from the input list that start with a vowel,
# the second with strings from the input list that start with a consonant,
# the third with strings that don't start with an alpha character
# Must be implemented recursively
def split_list(strlist: Optional[Node]) -> Tuple[Optional[Node], Optional[Node], Optional[Node]]:
    # write vowels in a list and compare the letters to the first index of the string list
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X',
                  'Y', 'Z']
    if strlist is None:
        return (None, None, None)
    lists = split_list(strlist.rest)
    if strlist.value[0] in vowels:
        return (Node(strlist.value, lists[0]), lists[1], lists[2])
    elif strlist.value[0] in consonants:
        return (lists[0], Node(strlist.value, lists[1]), lists[2])
    else:
        return (lists[0], lists[1], Node(strlist.value, lists[2]))
