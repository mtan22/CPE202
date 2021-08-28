# Project 1 - bears.py: Michelle Tan
# Instructor: Prof. Parkinson

# Given integer n, returns True or False based on reachability of goal
# See write up for "rules" for bears
def bears(n: int) -> bool:
    if n < 42:
        return False
    if n == 42:
        return True
    if n % 2 == 0:
        amount = n//2
        if bears(amount):
            return True
    if n % 3 == 0 or n % 4 == 0:
        str1 = (str(n)[len(str(n)) - 1])
        str2 = (str(n)[len(str(n)) - 2])
        num = int(str1)*int(str2)
        if num == 0:
            return False
        else:
            amount = n - num
            if bears(amount):
                return True
    if n % 5 == 0:
        amount = n - 42
        if bears(amount):
            return True
    return False
