#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : eyal , eyalmutzary , 206910432
# EXERCISE : intro2cs ex2 2021
# DESCRIPTION: A simple program that works like a simple calculator
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

def calculate_mathematical_expression(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == ':' and num2 != 0:
        return num1 / num2
    return None


def calculate_from_string(expression):
    num1, operation, num2 = expression.split()
    return calculate_mathematical_expression(
        float(num1), float(num2), operation)
