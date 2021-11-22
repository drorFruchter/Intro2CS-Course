from typing import List
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
    return check_divisior(b, x, b)

# Used for is_power
def check_divisior(b: int, x: int, c: int) -> bool:
    if x == b:
        return True
    elif b > x:
        return False
    else:
        return check_divisior(b*c, x, c)


def reverse(s: str) -> str:
    if s == '':
        return ''
    return reverse(s[1:]) + append_to_end('', s[0])


# --------- Part 2 ---------


print(is_power(1, 12))

