# Project 1 - perm_lex.py: Michelle Tan
# Instructor: Prof. Parkinson

from typing import List


# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in: str) -> List:
    perm_list = []
    if len(str_in) == 1:
        return [str_in]
    elif len(str_in) == 0:
        return []
    else:
        for i in str_in:
            for j in perm_gen_lex(str_in.replace(i, "", 1)):
                perm_list.append(i + j)

    perm_list = [perm_list[i] for i in range(len(perm_list)) if i == perm_list.index(perm_list[i])]
    perm_list.sort()

    return perm_list
