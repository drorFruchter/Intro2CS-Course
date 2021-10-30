#################################################################
# FILE : shapes.py
# WRITER : eyal , eyalmutzary , 206910432
# EXERCISE : intro2cs ex2 2021
# DESCRIPTION: A simple program that calculates the surface of a circle,
# triangle and a rectangle
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

import math


def circle_surface(r):
    return math.pi * (r**2)


def rectangle_surface(len1, len2):
    return len1 * len2


def triangle_surface(len_val):
    return (math.sqrt(3)/4)*(len_val**2)


def shape_area():
    option = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if option not in ["1", "2", "3"]:
        return None
    if option == '1':
        return circle_surface(float(input()))
    if option == '2':
        return rectangle_surface(float(input()), float(input()))
    else:
        return triangle_surface(float(input()))
