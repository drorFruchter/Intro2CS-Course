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
    return check_divisor(b, x, b)


# Used for is_power
def check_divisor(b: int, x: int, c: int) -> bool:
    if x == b:
        return True
    elif b > x:
        return False
    else:
        return check_divisor(int(log_mult(b,c)), x, c)


def reverse(s: str) -> str:
    if s == '':
        return ''
    return reverse(s[1:]) + append_to_end('', s[0])


# --------- Part 2 ---------


def play_hanoi(hanoi: Any, n: int, src: Any, dst: Any, temp: Any):
    if n == 1:
        hanoi.move(src, dst)
        return
    else:
        play_hanoi(hanoi, n-1, src, dst, temp)
        hanoi.move(src, temp)
        hanoi.move(dst, temp)
        hanoi.move(src, dst)
        # play_hanoi(hanoi, n-1, src, dst, temp)




# --------- Part 3 ---------

#

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
    pass