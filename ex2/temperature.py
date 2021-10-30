#################################################################
# FILE : temperature.py
# WRITER : eyal , eyalmutzary , 206910432
# EXERCISE : intro2cs ex2 2021
# DESCRIPTION: A simple program that checks if the temperature for Vormir
# is safe.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

def is_vormir_safe(extreme_temp, temp1, temp2, temp3):
    if temp1 > extreme_temp and temp2 > extreme_temp:
        return True
    elif temp1 > extreme_temp and temp3 > extreme_temp:
        return True
    elif temp2 > extreme_temp and temp3 > extreme_temp:
        return True
    return False

st = "dd\ndd\n"
print(st)