# CPE 202 Lab 1a: Michelle Tan
# Instructor: Prof. Parkinson

from typing import Optional
from typing import List


# Maybe_List (Optional[List]) is either
# Python List
# or
# None

# Maybe_integer (Optional[int]) is either
# integer
# or
# None

# Maybe_List -> Maybe_integer
def max_list_iter(int_list: Optional[List]) -> Optional[int]:
    maxNum = 0
    if int_list is None:
        raise ValueError

    elif len(int_list) == 0:
        return None

    elif len(int_list) > 0:
        for i in range(len(int_list)):
            if maxNum < int_list[i]:
                maxNum = int_list[i]

    return maxNum


# Maybe_List -> Maybe_List
def reverse_list(int_list: Optional[List]) -> Optional[List]:
    new_list = []
    if int_list is None:
        raise ValueError

    elif len(int_list) == 0:
        return None

    else:
        for i in range(len(int_list) - 1, -1, -1):
            new_list.append(int_list[i])

    return new_list


# Maybe_List -> None
def reverse_list_mutate(int_list: Optional[List]) -> None:
    if int_list is None:
        raise ValueError

    else:
        int_list[:] = int_list[::-1]
