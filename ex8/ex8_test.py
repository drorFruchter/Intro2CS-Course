import unittest
from puzzle_solver import *


def test_max_seen_cells():
    assert max_seen_cells([[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]] , 0, 0) == 1
    assert max_seen_cells([[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]] , 1, 0) == 0
    assert max_seen_cells([[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]] , 1, 2) == 5
    assert max_seen_cells([[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]] , 1, 1) == 3


def test_min_seen_cells():
    assert min_seen_cells([[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]], 0, 0) == 0
    assert min_seen_cells([[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]], 1, 0) == 0
    assert min_seen_cells([[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]], 1, 2) == 0
    assert min_seen_cells([[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]], 1, 1) == 1


def test_check_constraints():
    picture1 = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
    picture2 = [[0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    assert check_constraints(picture1, {(0, 3, 5), (1, 2, 5), (2, 0, 1)}) == 0
    assert check_constraints(picture2, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 1
    assert check_constraints(picture1, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 2


def test_solve_puzzle():
    assert solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 0)}, 3, 4) == [[0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    assert solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (2, 3, 5)}, 3, 4) == None
    assert solve_puzzle({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) == [[0, 0, 1], [1, 1, 1], [1, 1, 1] or [[1, 0, 1], [1, 1, 1], [1, 1, 1]]]


def test_how_many_solutions():
    assert how_many_solutions({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 1)}, 3, 4) == 1
    assert how_many_solutions({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) == 2
    assert how_many_solutions({(i, j, 0) for i in range(3) for j in range(3)}, 3, 3) == 1
    assert how_many_solutions(set(), 2, 2) == 16
    assert how_many_solutions({(0, 3, 3), (2, 0, 1)}, 3, 4) == 64


def test_generate_puzzle():
    assert generate_puzzle([[1, 0, 0], [1, 1, 1]]) == {(0, 0, 2), (1, 1, 3), (0, 1, 0), (0, 2, 0)}
    assert generate_puzzle([[1]]) == {(0, 0, 1)}


def main():
    test_max_seen_cells()
    test_min_seen_cells()
    test_check_constraints()
    test_solve_puzzle()
    test_how_many_solutions()



if __name__ == '__main__':
    main()
