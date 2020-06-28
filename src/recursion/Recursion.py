def factorial_iterate(num):
    rt = num
    while num >= 1:
        rt = rt * (num - 1)
        num -= 1
    return rt


def factorial_recursion(num):
    if num <= 2:
        return num
    else:
        return factorial_recursion(num - 1) * num


# Given a number N return the index value of the Fibonacci sequence,
# where the sequence is:
# 0,1,1,2,3,5,8,13,21,34,55,89,144....
#
def fibonacci_iterate(num):
    a, b = 0, 1
    for _ in range(num - 1):
        a, b = b, a + b
    return b


def fibonacci_recursion(num):
    if num < 2:
        return num
    else:
        return fibonacci_recursion(num - 1) + fibonacci_recursion(num - 2)


# Implement a function that reverses a string using
# iteration and then recursion!
def reverse_str_iteration(input_str):
    reversed_str = ""
    lst = list(input_str)
    while lst:
        reversed_str = reversed_str + lst.pop()
    return reversed_str


def reverse_str_recursion(input_str):
    if len(input_str) == 1:
        return input_str
    else:
        return input_str[-1] + reverse_str_recursion(input_str[:-1])
