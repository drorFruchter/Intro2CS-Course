from typing import List, Tuple, Set, Optional


# We define the types of a partial picture and a constraint (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]


# ---------- Prolog ----------


def create_default_picture(n: int, m: int) -> Picture:
    """
        Creates a picture of all -1
        :param n- row
        :param m - col
        :return Picture
    """
    picture = []
    for i in range(n):
        picture.append([])
        for _ in range(m):
            picture[i].append(-1)
    return picture


def append_constraints_set(picture: Picture, constraint_set: Set[Constraint])\
        -> List[List[int]]:
    """
        Appends a contraints set on a picture
        :param picture - Picture
        :param constraint_set - the Constraints set
        :return the updated picture
    """
    if constraint_set == set():
        return picture
    for constraint in constraint_set:
        picture[constraint[0]][constraint[1]] = constraint[2]
    return picture


def print_picture(picture: List[List[int]]) -> None:
    """
        prints a nice visual picture
        :param picture - picture
    """
    for i in range(len(picture)):
        for j in range(len(picture[i])):
            if picture[i][j] == -1:
                print(" ? " , end="")
            elif picture[i][j] == 0:
                print(" ■ " , end="")
            elif picture[i][j] == 1:
                print(" □ " , end="")
            else:
                print(" " + str(picture[i][j]) + " " , end="")
        print()


# ---------- Part 1 -----------


def _should_break(num: int, is_max: bool) -> bool:
    """
        if it encounters a 0 or -1
        :param num - the value of the index
        :param is_max - are we on is_max or is_min mode?
        :return should break or not
    """
    if is_max and num == 0:
        return True
    elif not is_max and num <= 0:
        return True
    return False


def _seen_row(row: List[int], col: int, is_max: bool):
    """
        loops on the row around the index
        :param row - int
        :param col - int
        :param is_max - is_max - are we on is_max or is_min mode?
        :return the number of indexes seen
    """
    count: int = 0
    for i in range(col, len(row), 1):
        if _should_break(row[i], is_max):
            break
        count += 1
    for i in range(col-1, -1, -1):
        if _should_break(row[i], is_max):
            break
        count += 1
    if row[col] != 0:
        count -= 1
    return count


def _seen_col(picture: Picture, row: int, col: int, is_max: bool):
    """
        same as seen row but for column
    """
    count: int = 0
    for i in range(row, len(picture), 1):
        if _should_break(picture[i][col], is_max):
            break
        count += 1
    for i in range(row, -1, -1):
        if _should_break(picture[i][col], is_max):
            break
        count += 1

    if picture[row][col] != 0:
        count -= 1
    return count


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    """
        sums all the max cells was seen - -1 counts as white
        :param picture - Picture
        :param row - int
        :param col - int
        :return the number of max cells seen
    """
    if picture[row][col] == 0:
        return 0
    else:
        return _seen_row(picture[row], col, True) +\
               _seen_col(picture, row, col, True)


def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    """
        sums all the min cells was seen - -1 counts as black
        :param picture - Picture
        :param row - int
        :param col - int
        :return the number of min cells seen
    """
    if picture[row][col] <= 0:
        return 0
    else:
        return _seen_row(picture[row], col, False) + \
            _seen_col(picture, row, col, False)


# ---------- Part 2 -----------


def check_constraints(picture: Picture, constraints_set: Set[Constraint])\
        -> int:
    """
        checks if the current picture is valid
        :param picture - Picture
        :param constraints_set - Contraint
        :return 0 - not valid,
                1 - exactly valid,
                2 - not valid on max, valid on min
    """
    status = 1
    if constraints_set == set():
        return 1

    for const in constraints_set:
        min_seen = min_seen_cells(picture, const[0], const[1])
        max_seen = max_seen_cells(picture, const[0], const[1])
        if const[2] < min_seen or const[2] > max_seen:
            return 0
        elif const[2] == min_seen and const[2] == max_seen:
            continue
        elif min_seen <= const[2] <= max_seen:
            status = 2
    return status


# ---------- Part 3 -----------


def formal_solution(picture: Picture) -> Optional[Picture]:
    """
        Change all values of a picture to be either 0 or 1
        :param picture - Picture
        :return the number of max cells seen
    """
    new_picture = []
    for i in range(len(picture)):
        new_picture.append([])
        for j in range(len(picture[i])):
            if picture[i][j] == 0:
                new_picture[i].append(0)
            else:
                new_picture[i].append(1)
    return new_picture


def _solve_puzzle_helper(picture: Picture,
                         ind: int,
                         constraints_set: Set[Constraint],
                         sol: List[Picture]) -> None:
    """
        Backtracking function to find a single solution to the puzzle
        :param picture - Picture
        :param ind - index pointer
        :param constraints_set - all the constraints
        :param sol - the first solution found (if there is)
    """
    check = check_constraints(picture, constraints_set)
    if ind == len(picture) * len(picture[0]):
        if check == 1 and len(sol) == 0:
            sol.append(formal_solution(picture))
        return

    row, col = ind // len(picture[0]), ind % len(picture[0])

    if picture[row][col] != -1:
        _solve_puzzle_helper(picture, ind + 1, constraints_set, sol)
        return

    for value in (0, 1):
        if len(sol) == 1 or check == 0:
            return
        picture[row][col] = value
        _solve_puzzle_helper(picture, ind + 1, constraints_set, sol)
    picture[row][col] = -1


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) \
        -> Optional[Picture]:
    """
        a function to solve the puzzle (with the helper function)
        :param constraints_set - all the constraints
        :param n - int
        :param m - int
        :return a solved puzzle or None
    """
    picture = create_default_picture(n, m)
    append_constraints_set(picture, constraints_set)
    sol = []
    _solve_puzzle_helper(picture, 0, constraints_set, sol)
    if len(sol) > 0:
        return sol[0]
    else:
        return None


# ---------- Part 4 -----------


def _count_solutions(picture: Picture,
                     ind: int,
                     constraints_set: Set[Constraint],
                     counter: List[int]) -> None:
    """
        a backtracking function to count how many solutions there are
        :param picture - Picture
        :param ind - index pointer
        :param constraints_set - all the constraints
        :param counter - counter of the solutions
    """
    check = check_constraints(picture, constraints_set)
    if ind == len(picture) * len(picture[0]):
        if check == 1:
            counter[0] += 1
        return

    row, col = ind // len(picture[0]), ind % len(picture[0])

    if picture[row][col] != -1:
        _count_solutions(picture, ind + 1, constraints_set, counter)
        return

    for value in (0, 1):
        if check == 0:
            return
        picture[row][col] = value
        _count_solutions(picture, ind + 1, constraints_set, counter)
    picture[row][col] = -1


def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int)\
        -> int:
    """
        a funtion the finds how many soultions there are
        :param constraints_set - Consrtraint
        :param n - rows
        :param m - columns
        :return the amount of solutions to the puzzle
    """
    picture = create_default_picture(n, m)
    append_constraints_set(picture, constraints_set)
    counter = [0]
    _count_solutions(picture, 0, constraints_set, counter)
    return counter[0]


# ---------- Part 5 -----------


def _prep_picture(picture: Picture):
    """
        changes every cell that is not 0 to -1
        :param picture - Picture
    """
    for row in range(len(picture)):
        for col in range(len(picture[row])):
            if picture[row][col] == 1:
                picture[row][col] = -1


def _loop_row(picture: Picture, row: int, col: int):
    """
        by index, changes every seen cell in row to -2
        :param picture - Picture
        :param row - int
        :param col - int
    """
    for i in range(col+1, len(picture[row]), 1):
        if picture[row][i] == 0:
            break
        picture[row][i] = -2
    for i in range(col-1, -1, -1):
        if picture[row][i] == 0:
            break
        picture[row][i] = -2


def _loop_col(picture: Picture, row: int, col: int):
    """
        by index, changes every seen col to -2
        :param picture - Picture
        :param row - int
        :param col - int
    """
    for i in range(row+1, len(picture), 1):
        if picture[i][col] == 0:
            break
        picture[i][col] = -2
    for i in range(row, -1, -1):
        if picture[i][col] == 0:
            break
        picture[i][col] = -2


def copy_picture(picture: Picture) -> Picture:
    """
        gets a picture and returns a copy of it
        :param picture - Picture
        :return a copy of the picture
    """
    new_picture = []
    for i in range(len(picture)):
        new_picture.append([])
        for j in range(len(picture[i])):
            new_picture[i].append(picture[i][j])
    return new_picture


def generate_puzzle(picture: Picture) -> Set[Constraint]:
    """
        generates a set of constraints by a puzzle
        :param picture - Picture
        :return a set of constraints
    """
    constraint = set()
    picture_copy = copy_picture(picture)
    _prep_picture(picture_copy)
    for row in range(len(picture_copy)):
        for col in range(len(picture_copy[row])):
            if picture_copy[row][col] == -1:
                value = max_seen_cells(picture_copy, row, col)
                picture_copy[row][col] = value
                _loop_row(picture_copy, row, col)
                _loop_col(picture_copy, row, col)
                constraint.add((row, col, value))
            elif picture_copy[row][col] == 0:
                constraint.add((row, col, 0))
    return constraint


