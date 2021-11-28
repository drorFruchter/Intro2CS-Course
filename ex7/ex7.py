#################################################################
# FILE : ex7.py
# WRITER : eyal , eyalmutzary , 206910432
# EXERCISE : intro2cs ex7 2021
# DESCRIPTION: Recursions!
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################
from typing import Any, List
from ex7_helper import *


# --------- Part 1 ---------


def mult(x: float, y: int) -> float:
    """
        multiplies x * y
        :param x - float
        :param y - int
        :return x * y
    """
    if y == 0:
        return 0
    return add(x, mult(x, int(subtract_1(y))))


def is_even(n: int) -> bool:
    """
        Checks if n is even
        :param n - int
        :return is even?
    """
    if n == 1:
        return False
    elif n == 0:
        return True
    return is_even(subtract_1(subtract_1(n)))


def log_mult(x: float, y: int) -> float:
    """
        x * y, but O(log(n))
        :param x - float
        :param y - int
        :return x * y
    """
    if y == 0:
        return 0
    if is_odd(y):
        return add(log_mult(x, int(add(y, -1))), x)
    else:
        return add(log_mult(x, divide_by_2(y)), log_mult(x, divide_by_2(y)))


def is_power(b: int, x: int) -> bool:
    """
        checks if b is power of x:
        :param b - int
        :param x - int
        :return is power?
    """
    if x == 1:
        return True
    elif b == 0 and x > 1:
        return False
    elif b == 0 and (x == 0 or x == 1):
        return True
    elif b > x:
        return False

    return is_power_helper(b, x, b, b)


def is_power_helper(b: int, x: int, c: int, new_b: int) -> bool:
    """
        checks if b is power of x:
        :param b - int
        :param x - int
        :param c = b
        :param new_b = b
        :return is power?
    """
    if x == b:
        return True
    elif b > x:
        return False
    if b == add(x, 1):
        return False
    else:
        power = int(log_mult(b,new_b))
        is_power_helper(power, x, c, power)
        b = int(log_mult(b, c))
        return is_power_helper(b, x, c, c) or False


def reverse(s: str) -> str:
    """
        reverses a string
        :param s - string
        :return a reversed string
    """
    return reverse_helper(s, len(s), '',)


def reverse_helper(s: str, n: int, new_s: str) -> str:
    """
        helper funtion to reverse
        :param s - string
        :param n - len of s
        :param new_s - the new string
        :return revered string s
    """
    if n == 0:
        return new_s
    else:
        return reverse_helper(s, n-1, append_to_end(new_s, s[n-1]))


# --------- Part 2 ---------


def play_hanoi(hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> None:
    """
        Solves the tower of Hanoi. Gets objects from hanoi_game.py
        :param hanoi - float
        :param n - int
        :param src - Any
        :param dst - Any
        :param temp - Any
    """
    if n <= 0:
        return
    if n == 1:
        hanoi.move(src, dst)
    else:
        play_hanoi(hanoi, n-1, src, temp, dst)
        hanoi.move(src, dst)
        play_hanoi(hanoi, n-1, temp, dst, src)


# --------- Part 3 ---------


def number_of_ones(n:int) -> int:
    """
        conts the number of ones from 1 to n
        :param n - int
        :return number of ones
    """
    if n == 0:
        return 0
    else:
        return number_of_ones(n-1) + count_ones(n)


def count_ones(n: int) -> int:
    """
        counts the number of ones in n
        :param n - int
        :return number of ones in n
    """
    if n == 0:
        return 0
    else:
        if n%10 == 1:
            return number_of_ones(n//10) + 1
        else:
            return number_of_ones(n//10)


def compare_2d_lists(l1: List[List[int]], l2: List[List[int]]) -> bool:
    """
        deep compare 2D lists
        :param l1 - 2D list
        :param l2 - 2D list
        :return are they equal?
    """
    if len(l1) != len(l2):
        return False
    else:
        return compare_2d_lists_helper(l1, l2, len(l1))


def compare_2d_lists_helper(l1: List[List[int]], l2: List[List[int]], index: int) -> bool:
    """
        an helper function
        :param l1 - 2D list
        :param l2 - 2D list
        :return are they equal?
    """
    if index == 0:
        return True
    else:
        return compare_2d_lists_helper(l1, l2, index-1) \
               and len(l1[index-1]) == len(l2[index-1]) \
               and compare_1d_lists(l1[index-1], l2[index-1], index)


def compare_1d_lists(l1: List[int], l2: List[int], index: int) -> bool:
    """
        Compare 1D list
        :param l1 - 1D list
        :param l2 - 1D list
        :return are they equal?
    """
    if index == -1:
        return True
    else:
        if len(l1) == 0 and len(l2) == 0:
            return True
        return compare_1d_lists(l1, l2, index-1) and l1[index-1] == l2[index-1]


def magic_list(n: int) -> List[Any]:
    """
        Makes a "magic" list
        :param n - the depth of the list
        :return a magic list
    """
    if n == 0:
        return []
    elif n == 1:
        return [[]]
    return magic_list_helper(n-1, [])


def magic_list_helper(n: int, lst: List[Any]) -> List[Any]:
    """
        an helper function
        :param n - the depth of the list
        :param lst - an empty list
        :return a magic lst
    """
    if n == 0:
        lst.append([])
    else:
        magic_list_helper(n-1, lst)
        lst.append([])
        magic_list_helper(n-1, lst[n])
        return lst
