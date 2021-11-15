from typing import List, Dict
from sys import argv


def check_input_args(args: List[str]):
    """
        :param args - List of strings of the cmd params.
        :return None if they valid, or Error if not.
        It should be: word_file,matrix_file, output_file, directions
    """

    if len(args) == 4 \
            and args[0] == "word_file" \
            and args[1] == "matrix_file" \
            and args[2] == "output_file" \
            and args[3] == "directions":
        return None
    return "Error, params were invalid."


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


def read_directions_file(filename: str):
    """
        Reads the directions file and returns a string.
        :param filename - the name of the file to read.
        :return a string with some of the letters: 'udrlwxyz'.
    """
    with open(filename + '.txt') as reader:
        directions = str(reader.readlines())
    return directions


def count_occurrences_in_series(word: str, letters: str):
    """
        Counts the number of occurrences of a word in a string
        :param word - the word to look for.
        :param letters - the collection of letters.
        :return the amount of occurrences the word had in the letters.
    """
    if word == "" or letters == "":
        return 0

    i: int = len(word)
    count: int = 0
    while i <= len(letters):
        if word == letters[i-len(word): i]:
            count += 1
        i += 1
    return count


def reverse_strings_in_list(lst: List[str]):
    """
        Reverese every string in the list
        :param lst - a list of strings
        :return a new list with every string reversed.
    """
    return [st[::-1] for st in lst]


def handle_direction_d_or_u(matrix:List[List[str]], series_list: List[str]):
    """
        Scans a matrix down, and adds a series of letters for every column
        :param matrix - a 2D list to scan
        :param series_list - a list to add the new strings
        :return updated series_list
    """
    st: str = ""
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            st += matrix[row][col]
        series_list.append(st)
        st = ""
    return series_list


def handle_direction_w_or_z(matrix: List[List[str]], series_list: List[str]):
    """
        Scans a matrix w direction, and adds the series of letters.
        :param matrix - a 2D list to scan
        :param series_list - a list to add the new strings
        :return updated series_list
    """
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
    """
        Scans a matrix x direction, and adds the series of letters.
        :param matrix - a 2D list to scan
        :param series_list - a list to add the new strings
        :return updated series_list
    """
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
    """
        Creates a list of letter series
        :param matrix - a 2D list to scan
        :param direction - the direction to scan.
        :return list of the scanned strings by the direction
    """
    series_list: List[str] = []
    if matrix == []:
        return []

    elif direction == "r" or direction == "l":
        for row in matrix:
            series_list.append(''.join(row))

    elif direction == "d" or direction == "u":
        handle_direction_d_or_u(matrix, series_list)

    elif direction == 'w' or direction == 'z':
        handle_direction_w_or_z(matrix, series_list)

    elif direction == 'x' or direction == 'y':
        handle_direction_x_or_y(matrix, series_list)

    if direction == 'l' or direction == 'u' \
            or direction == 'z' or direction == 'y':
        series_list = reverse_strings_in_list(series_list)

    return series_list


def search_word_single_direction(word: str,
                                 matrix: List[List[str]],
                                 direction: str):
    """
        counts the occurrences of a word in list of strings
        :param word - the word to look for.
        :param matrix - a 2D list.
        :param direction - the direction to scan
        :return the number of occurrences in the list.
    """
    series_list = get_series_list_by_direction(matrix, direction)
    count: int = 0
    for series in series_list:
        count += count_occurrences_in_series(word, series)
    return count


def find_words_in_matrix(word_list: List[str],
                         matrix: List[List[str]],
                         directions: str):
    """
        counts occurrences of words in a matrix by many directions
        :param word_list - the list of words to look for.
        :param matrix - a 2D list.
        :param directions - a string of all directions to check.
        :return a dictionary of the type: {word: occurrences}
    """
    occ_dict: Dict[str: int] = dict()
    for word in word_list:
        occurrences: int = 0
        for direction in directions:
            occurrences += search_word_single_direction(word, matrix, direction)
        if occurrences > 0:
            occ_dict[word] = occurrences
    return occ_dict


def convert_result_to_list(results):
    """
        Convert a dictionary type result to list of tuples
        :param results - a dictionary of: {word: occurrences}
        :return a list from the type: List[(word, occurrences)]
    """
    new_lst: List[(str, int)] = []
    for word in results:
        new_lst.append((word, results[word]))
    return new_lst


def write_output_file(results, output_filename: str):
    """
        Writes in the file the results.
        :param results - a list from the form: List[(word, occurrences)]
        :return None
    """
    f = open(output_filename + ".txt", "w")
    st = ""
    for couple in results:
        st += couple[0] + "," + str(couple[1]) + "\n"
    f.write(st)
    f.close()


def main():
    if check_input_args(argv[1:]) is None:
        words, mat, output, direct = argv[1:]
        word_list = read_wordlist_file(words)
        matrix = read_matrix_file(mat)
        directions: str = read_directions_file(direct)
        results = find_words_in_matrix(word_list, matrix, directions)
        write_output_file(convert_result_to_list(results), output)


if __name__ == "__main__":
    main()
