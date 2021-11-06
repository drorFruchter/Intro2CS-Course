from typing import List
import os


def check_input_args(args: List[str]):
    """
        :param args - List of strings of the cmd params.
        :return None if they valid, or Error if not.
        It should be: word_file,matrix_file, output_file, directions
    """
    if args[0] == "word_file" \
            and args[1] == "matrix_file" \
            and args[2] == "output_file" \
            and args[3] == "directions":
        return None
    return "Error, param name wasn't valid."


def read_wordlist_file(filename: str):
    """
        Reads the word_list file and returns the list of words.
        :param filename - the name of the file to read.
        :return list of the words in the file.
    """
    with open(filename + '.txt') as reader:
        words = [word.replace('\n', '') for word in reader.readlines()]
    return words


def read_matrix_file(filename: str):
    """
        Reads the matrix file and returns the 2D list of letters.
        :param filename - the name of the file to read.
        :return 2D list of the letters in the file.
    """
    with open(filename + '.txt') as reader:
        matrix = [[letter for letter in row
                   if letter != ',' and letter != '\n']
                  for row in reader.readlines()]
    return matrix


def count_occurrences_in_series(word: str, letters: str):
    """
        Counts the number of occurrences of a word in a string
        :param word - the word to look for.
        :param letters - the collection of letters.
        :return the amount of occurrences the word had in the letters.
    """
    if word == "" or letters == "":
        return None

    i: int = len(word)
    count: int = 0
    while i <= len(letters):
        if word == letters[i-len(word): i]:
            count += 1
        i += 1
    return count


def reverse_strings_in_list(lst: List[str]):
    return [st[::-1] for st in lst]


def handle_direction_d_or_u(matrix:List[List[str]], series_list: List[str]):
    st: str = ""
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            st += matrix[row][col]
        series_list.append(st)
        st = ""
    return series_list


def handle_direction_w_or_z(matrix: List[List[str]], series_list: List[str]):
    st: str = ""
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            st += matrix[row][col]
            col -= 1
            if col < 0:
                break
        series_list.append(st)
        st = ""
    starting_row = 1
    for col in range(len(matrix[0]), 0, -1):
        col_length = len(matrix[0])-1
        for row in range(starting_row,len(matrix)):
            st += matrix[row][col_length]
            col_length -= 1
            if col_length < 0:
                break
        starting_row += 1
        series_list.append(st)
        st = ""


def handle_direction_x_or_y(matrix: List[List[str]], series_list: List[str]):
    st: str = ""
    for col in range(len(matrix[0])):
        row = len(matrix) - 1
        for _ in range(len(matrix)):
            st += matrix[row][col]
            col -= 1
            row -= 1
            if row < 0 or col < 0:
                break
        series_list.append(st)
        st = ""
    for row in range(len(matrix)-1):
        col = len(matrix[0]) - 1
        for _ in range(len(matrix)):
            st += matrix[row][col]
            col -= 1
            row -= 1
            if row < 0 or col < 0:
                break
        series_list.append(st)
        st = ""

def get_series_list_by_direction(matrix:List[List[str]], direction):
    series_list: List[str] = []
    if matrix == []:
        return []

    elif direction == "r" or direction == "l":
        for row in matrix:
            series_list.append(''.join(row))

    elif direction == "d" or direction == "u":
        handle_direction_d_or_u(matrix,series_list)

    elif direction == 'w' or direction == 'z':
        handle_direction_w_or_z(matrix, series_list)

    elif direction == 'x' or direction == 'y':
        handle_direction_x_or_y(matrix, series_list)

    if direction == 'l' or direction == 'u' \
            or direction == 'z' or direction == 'y':
        series_list = reverse_strings_in_list(series_list)

    return series_list




# def search_word_single_direction(word: str,
#                                  matrix: List[List[str]],
#                                  direction: str):
#     pass




# def find_words_in_matrix(word_lsit: List[str],
#                          matrix: List[List[str]],
#                          directions: str):


matrix = read_matrix_file("matrix_file")
print(get_series_list_by_direction(matrix, "x"))