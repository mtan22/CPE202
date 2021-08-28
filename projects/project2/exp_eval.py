# Project 2: Michelle Tan
# Instructor: Prof. Parkinson
# Date: 2/3/2021

from typing import Any

from stack_array import Stack


# You should not change this Exception class!
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str: str) -> Any:
    """Evaluates a postfix expression"""
    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    stack = Stack(30)
    if input_str == "":
        raise PostfixFormatException('Insufficient operands')
    op_list = ["+", "-", "*", "/", "<<", ">>", "**"]
    split_list = input_str.split()
    for i in split_list:
        new_val = i.lstrip("-")
        new_val = new_val.replace(".", "", 1)
        if i in op_list:
            try:
                num_val = stack.pop()
                num_val_initial = stack.pop()
            except IndexError:
                raise PostfixFormatException("Insufficient operands")
            if i == "+":
                stack.push(num_val_initial + num_val)
            if i == "-":
                stack.push(num_val_initial - num_val)
            if i == "*":
                stack.push(num_val_initial * num_val)
            if i == "/":
                if num_val == 0:
                    raise ValueError("0 not divisible")
                stack.push(num_val_initial / num_val)
            if i == "**":
                stack.push(num_val_initial ** num_val)
            if i == "<<":
                t1 = type(num_val)
                t2 = type(num_val_initial)
                if t1 == float or t2 == float:
                    raise PostfixFormatException("Illegal bit shift operand")
                stack.push(num_val_initial << num_val)
            if i == ">>":
                t1 = type(num_val)
                t2 = type(num_val_initial)
                if t1 == float or t2 == float:
                    raise PostfixFormatException("Illegal bit shift operand")
                stack.push(num_val_initial >> num_val)
        elif new_val.isdigit():
            if "." in i:
                stack.push(float(i))
            else:
                stack.push(int(i))
        else:
            raise PostfixFormatException("Invalid token")
    val = stack.pop()
    if not stack.is_empty():
        raise PostfixFormatException("Too many operands")
    return val


def infix_to_postfix(input_str: str) -> Any:
    """Converts an infix expression to an equivalent postfix expression"""
    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression """
    stack = Stack(30)
    if input_str == '':
        return ''
    op_list = ["+", "-", "*", "/", "<<", ">>", "**"]
    order = {}
    order["+"] = 1
    order["-"] = 1
    order["*"] = 2
    order["/"] = 2
    order["**"] = 3
    order["<<"] = 4
    order[">>"] = 4
    pfix_str = ''
    split_list = input_str.split()
    for i in split_list:
        new_val = i.lstrip("-")
        new_val = new_val.replace(".", "", 1)
        if new_val.isdigit() and pfix_str == "":
            pfix_str = pfix_str + i
        elif i in op_list:
            if not stack.is_empty():
                p = stack.peek()
            while 0 < stack.size():
                p = stack.peek()
                if p == "(":
                    break
                if i == "**":
                    if order[p] <= order[i]:
                        break
                    else:
                        p1 = stack.pop()
                        pfix_str = pfix_str + " " + p1
                elif order[p] < order[i]:
                    break
                else:
                    p2 = stack.pop()
                    pfix_str = pfix_str + " " + p2
            stack.push(i)
        elif i == "(":
            stack.push(i)
        elif new_val.isdigit():
            pfix_str = pfix_str + " " + i
        elif i == ")":
            p = stack.peek()
            while p != "(":
                pfix_str = pfix_str + " " + stack.pop()
                if not stack.is_empty():
                    p = stack.peek()
            stack.pop()
    while not stack.is_empty():
        pop3 = stack.pop()
        pfix_str = pfix_str + " " + pop3
    return pfix_str


def prefix_to_postfix(input_str: str) -> Any:
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""
    stack = Stack(30)
    if input_str == "":
        return ("")
    op_list = ["+", "-", "*", "/", "<<", ">>", "**"]
    split_list = input_str.split()
    track = len(split_list) - 1
    while track >= 0:
        new_val = split_list[track].lstrip("-")
        new_val = new_val.replace(".", "", 1)
        if new_val.isdigit():
            stack.push(split_list[track])
            track = track - 1
        elif split_list[track] in op_list:
            first = stack.pop()
            second = stack.pop()
            stack.push(first + " " + second + " " + split_list[track])
            track = track - 1
        else:
            break
    postfix = stack.pop()
    return postfix
