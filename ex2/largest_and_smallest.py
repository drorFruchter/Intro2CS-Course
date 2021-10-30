#################################################################
# FILE : largest_and_smallest.py
# WRITER : eyal , eyalmutzary , 206910432
# EXERCISE : intro2cs ex2 2021
# DESCRIPTION: A simple program that finds the smallest and largest numbers
#              by the input
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: Submission test inputs with \n and it causes an error,  but a
#        regular input would work.
#################################################################

def largest_and_smallest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        largest = num1
        if num2 >= num3:
            smallest = num3
        else:
            smallest = num2
    elif num2 >= num1 and num2 >= num3:
        largest = num2
        if num1 >= num3:
            smallest = num3
        else:
            smallest = num1
    else:
        largest = num3
        if num1 >= num2:
            smallest = num2
        else:
            smallest = num1
    return largest, smallest


def check_largest_and_smallest():
    if largest_and_smallest(17, 1, 6) != (17, 1)\
            and largest_and_smallest(1, 17, 6) != (17, 1)\
            and largest_and_smallest(1, 1, 2) != (2, 1)\
            and largest_and_smallest(1.5, 1, 2.6) != (2.6, 1)\
            and largest_and_smallest(0, 0, 0) != (0, 0):
        return False
    return True
