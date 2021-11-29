from typing import List, Tuple, Set, Optional


# We define the types of a partial picture and a constraint (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]


# ---------- Prolog ----------


def create_default_picture(n: int, m: int) -> List[List[int]]:
    picture = []
    for i in range(n):
        picture.append([])
        for _ in range(m):
            picture[i].append(-1)
    return picture


def add_constraints_set(n: int, m: int, constraint_set: Set[Constraint]) -> List[List[int]]:
    picture = create_default_picture(n, m)
    for constraint in constraint_set:
        picture[constraint[0]][constraint[1]] = constraint[2]
    return picture


def print_picture(picture: List[List[int]]) -> None:
    for i in range(len(picture)):
        for j in range(len(picture[i])):
            if picture[i][j] == -1:
                print(" ? " , end="")
            # elif picture[i][j] == 0:
            #     print(" ■ " , end="")
            # elif picture[i][j] == 1:
            #     print(" □ " , end="")
            else:
                print(" " + str(picture[i][j]) + " " , end="")
        print()


# constraints_set = {(0, 0, 0), (0, 3, 3), (1, 2, 5), (2, 0, 1)}
# picture = add_constraints_set(3,5, constraints_set)
# print_picture((picture))


# ---------- Part 1 ----------


def _should_break(num: int, is_max: bool) -> bool:
    if is_max and num == 0:
        return True
    elif not is_max and num <= 0:
        return True
    return False


def _seen_row(row: List[int], col: int, is_max: bool):
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


# tested
def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    if picture[row][col] == 0:
        return 0
    else:
        return _seen_row(picture[row], col, True) +\
               _seen_col(picture, row, col, True)


# tested
def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    if picture[row][col] <= 0:
        return 0
    else:
        return _seen_row(picture[row], col, False) + \
            _seen_col(picture, row, col, False)


# tested
def check_constraints(picture: Picture, constraints_set: Set[Constraint]) -> int:
    status = 1
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



def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    ...


def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    ...


def generate_puzzle(picture: Picture) -> Set[Constraint]:
    ...
