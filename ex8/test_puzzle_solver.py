from puzzle_solver import *

picture1 = [[-1, 0, 1, -1],
            [0, 1, -1, 1],
            [1, 0, 1, 0]]
picture2 = [[0, 0, 1, 1],
            [0, 1, 1, 1],
            [1, 0, 1, 0]]


def test_max_seen_cells():
    assert max_seen_cells(Picture, 0, 0) == 1
    assert max_seen_cells(Picture, 1, 0) == 0
    assert max_seen_cells(Picture, 2, 0) == 1
    assert max_seen_cells(Picture, 0, 1) == 0
    assert max_seen_cells(Picture, 2, 3) == 0
    assert max_seen_cells(Picture, 0, 3) == 3
    assert max_seen_cells(Picture, 2, 2) == 3
    assert max_seen_cells(Picture, 1, 1) == 3
    assert max_seen_cells(Picture, 0, 2) == 4
    assert max_seen_cells(Picture, 1, 2) == 5
    assert type(max_seen_cells(Picture, 1, 2)) == int


def test_min_seen_cells():
    assert min_seen_cells(Picture, 0, 0) == 0
    assert min_seen_cells(Picture, 0, 1) == 0
    assert min_seen_cells(Picture, 0, 2) == 1
    assert min_seen_cells(Picture, 0, 3) == 0
    assert min_seen_cells(Picture, 1, 0) == 0
    assert min_seen_cells(Picture, 1, 2) == 0
    assert min_seen_cells(Picture, 1, 1) == 1
    assert type(min_seen_cells(Picture, 1, 1)) is int


def test_check_constraints():
    assert check_constraints(picture1, {(0, 3, 5), (1, 2, 5), (2, 0, 1)}) == 0
    assert check_constraints(picture2, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 1
    assert check_constraints(picture1, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 2
    assert type(check_constraints(picture1, {(0, 3, 3), (1, 2, 5), (2, 0, 1)})) is int


def test_solve_puzzle():
    assert solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 0)}, 3, 4) ==\
           [[0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    assert solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (2, 3, 5)}, 3, 4) is None
    assert solve_puzzle({(0, 0, 3), (0, 1, 0)}, 2, 2) is None
    assert solve_puzzle({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) in [[[0, 0, 1], [1, 1, 1], [1, 1, 1]], [[1, 0, 1], [1, 1, 1], [1, 1, 1]]]
    assert solve_puzzle(set(), 3, 3) is not None
    assert solve_puzzle({(i, j, 0) for i in range(3) for j in range(3)}, 3, 3) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert type(solve_puzzle({(i, j, 0) for i in range(3) for j in range(3)}, 3, 3)) is list


def test_how_many_solutions():
    assert how_many_solutions({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 1)}, 3, 4) == 1
    assert how_many_solutions({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3)  == 2
    assert how_many_solutions({(i, j, 0) for i in range(3) for j in range(3)}, 3, 3) == 1
    assert how_many_solutions(set(), 2, 2) == 16
    assert how_many_solutions(set(), 3, 4) == 4096
    assert how_many_solutions({(0, 3, 3), (2, 0, 1)}, 3, 4) == 64
    assert how_many_solutions(set(), 1, 1) == 2
    assert how_many_solutions({(0, 0, 1)}, 1, 1) == 1


def test_generate_puzzle():
    picture = [[1, 0, 0], [1, 1, 1]]
    cons_lst = [{(0, 0, 2), (1, 2, 3)},
                {(1, 0, 4), (0, 1, 0), (0, 2, 0)},
                {(1, 0, 4), (0, 0, 2), (0, 2, 0)},
                {(1, 0, 4), (1, 1, 3), (0, 2, 0)},
                {(1, 0, 4), (1, 1, 3), (1, 2, 3)},
                {(1, 0, 4), (0, 1, 0), (1, 2, 3)},
                {(0, 0, 2), (1, 1, 3), (0, 1, 0), (0, 2, 0)}]
    assert generate_puzzle(picture) in cons_lst
