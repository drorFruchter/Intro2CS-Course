#################################################################
# FILE : quadratic_equation.py
# WRITER : eyal , eyalmutzary , 206910432
# EXERCISE : intro2cs ex2 2021
# DESCRIPTION: A simple program that solves quadratic equations
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED: Wikipedia
# NOTES: Submission test inputs with \n and it causes an error,  but a
# regular input would work.
#################################################################

import math


def quadratic_equation(a, b, c):
    root_exp = b**2 - (4*a*c)
    if root_exp < 0:
        return None, None
    score1 = (-b - math.sqrt(root_exp)) / 2*a
    score2 = (-b + math.sqrt(root_exp)) / 2*a
    if score1 == score2:
        return score1, None
    return score1, score2


def quadratic_equation_user_input():
    a, b, c = input("Insert coefficients a, b, and c: ").split()
    if float(a) == 0:
        print("The parameter 'a' may not equal 0")
        return None
    score1, score2 = quadratic_equation(float(a), float(b), float(c))
    if score1 and score2:
        print("The equation has 2 solutions: " + str(score1) + " and " +
              str(score2))
    elif score1:
        print("The equation has 1 solution: " + str(score1))
    else:
        print("The equation has no solutions")

