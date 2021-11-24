from typing import Any, List
from ex7_helper import *

# --------- Part 1 ---------


def mult(x: float, y: int) -> float:
    if y == 0:
        return 0
    return add(x, mult(x, int(subtract_1(y))))


def is_even(n: int) -> bool:
    if n == 1:
        return False
    elif n == 0:
        return True
    return is_even(subtract_1(subtract_1(n)))


def log_mult(x: float, y: int) -> float:
    if y == 0:
        return 0
    if is_odd(y):
        return add(log_mult(x, int(add(y, -1))), x)
    else:
        return add(log_mult(x, divide_by_2(y)), log_mult(x, divide_by_2(y)))


def is_power(b: int, x: int) -> bool:
    if b == 0 or b == 1 or x == 0 or x == 1:
        return True
    return is_power_helper(b, x, b)


def is_power_helper(b: int, x: int, c: int) -> bool:
    if x == b:
        return True
    elif b > x:
        return False
    else:
        return is_power_helper(int(log_mult(b,c)), x, c)


def reverse(s: str) -> str:
    return reverse_helper(s, len(s), '',)


def reverse_helper(s: str, n: int, new_s: str) -> str:
    if n == 0:
        return new_s
    else:
        return reverse_helper(s, n-1, append_to_end(new_s, s[n-1]))


# --------- Part 2 ---------


def play_hanoi(hanoi: Any, n: int, src: Any, dst: Any, temp: Any):
    if n == 1:
        hanoi.move(src, dst)
    else:
        play_hanoi(hanoi, n-1, src, dst, temp)
        hanoi.move(src, temp)
        hanoi.move(dst, temp)
        play_hanoi(hanoi, n-1, temp, src, dst)


# --------- Part 3 ---------


def number_of_ones(n:int) -> int:
    if n == 0:
        return 0
    else:
        return number_of_ones(n-1) + count_ones(n)


def count_ones(n: int) -> int:
    if n == 0:
        return 0
    else:
        if n%10 == 1:
            return number_of_ones(n//10) + 1
        else:
            return number_of_ones(n//10)


def compare_2d_lists(l1: List[List[int]], l2: List[List[int]]) -> bool:
    if len(l1) != len(l2):
        return False
    else:
        return compare_2d_lists_helper(l1, l2, len(l1))


def compare_2d_lists_helper(l1: List[List[int]], l2: List[List[int]], index: int) -> bool:
    if index == 0:
        return True
    else:
        return compare_2d_lists_helper(l1, l2, index-1) \
               and len(l1[index-1]) == len(l2[index-1]) \
               and compare_1d_lists(l1[index-1], l2[index-1], index)


def compare_1d_lists(l1: List[int], l2: List[int], index: int) -> bool:
    if index == -1:
        return True
    else:
        if len(l1) == 0 and len(l2) == 0:
            return True
        return compare_1d_lists(l1, l2, index-1) and l1[index-1] == l2[index-1]





def exp_n_x(n, x):
    if n < 0:
        return None
    elif n == 0:
        return 1
    elif n == 1:
        return x+1
    elif n > 1:
        return exp_n_x(n-1, x) + ((x**n) / factorial(n))


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n





# def helper(n, k, path, lst):
#     if n == 0 and k == 0:
#         lst.append(path)
#     if n > 0:
#         helper(n-1, k, path + "r", lst)
#     if k > 0:
#         helper(n, k-1, path + "u", lst)
#
#
# def up_and_right(n, k, lst):
#     path = ''
#     helper(n, k, path, lst)
#     return lst
