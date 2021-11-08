import unittest
from typing import List
from cartoonify import *

def main():
    test_seperate_channels()
    test_rotate_90()
    test_combine_channels()
    test_RGB2grayscale()


def test_rotate_90():
    assert rotate_90([[1, 2, 3], [4, 5, 6]], 'R') == [[4, 1], [5, 2], [6, 3]]
    assert rotate_90([[1, 2, 3], [4, 5, 6]], 'L') == [[3, 6], [2, 5], [1, 4]]
    assert rotate_90([[1, 2, 3], [4, 5, 6], [1, 9, 6], [7, 2, 6]], 'R') == [[7, 1, 4, 1], [2, 9, 5, 2], [6, 6, 6, 3]]
    assert rotate_90([[1, 2, 3, 5, 6, 7], [4, 5, 6, 3, 7, 5]], 'R') == [[4, 1], [5, 2], [6, 3], [3, 5], [7, 6], [5, 7]]
    assert rotate_90([[1],[2],[1],[2]], 'R') == [[2, 1, 2, 1]]
    assert rotate_90([[1, 2, 3]], 'R') == [[1], [2], [3]]


def test_seperate_channels():
    assert separate_channels([[[1, 2]]]) == [[[1]], [[2]]]
    assert separate_channels([[[1, 2], [3, 4]]]) == [[[1, 3]], [[2, 4]]]
    assert separate_channels([[[1, 2], [3, 4]], [[5, 6]]]) == [[[1, 3], [5]], [[2, 4], [6]]]


def test_combine_channels():
    assert combine_channels([[[]]]) == [[[]]]
    assert combine_channels([[[1]]]) == [[[1]]]
    assert combine_channels([[[1]], [[2]]]) == [[[1, 2]]]
    assert combine_channels([[[1]], [[2]], [[3]]]) == [[[1, 2, 3]]]
    assert combine_channels([[[1, 2]], [[3, 4]]]) == [[[1, 3], [2, 4]]]
    assert combine_channels([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) == [[[1, 5], [2, 6]], [[3, 7], [4, 8]]]


def test_RGB2grayscale():
    assert RGB2grayscale([[[0, 0, 0]]]) == [[0]]
    assert RGB2grayscale([[[100, 180, 240]]]) == [[163]]
    assert RGB2grayscale([[[100, 180, 240], [100, 180, 240], [100, 180, 240]]]) == [[163, 163, 163]]
    assert RGB2grayscale([[[100, 180, 240], [100, 180, 240], [100, 180, 240]],
                          [[100, 180, 240], [100, 180, 240], [100, 180, 240]]]) == [[163, 163, 163], [163, 163, 163]]


if __name__ == '__main__':
    main()
