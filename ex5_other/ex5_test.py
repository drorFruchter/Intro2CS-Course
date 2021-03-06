import unittest
from typing import List
from cartoonify import *

def main():
    test_seperate_channels()
    test_rotate_90()
    test_combine_channels()
    test_RGB2grayscale()
    test_bilinear_interpolation()
    test_apply_kernel()
    test_get_edges()
    test_quantize()
    test_quantize_colored_image()
    test_add_mask()


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


def test_bilinear_interpolation():
    assert bilinear_interpolation([[0, 64], [128, 255]], 0, 0) == 0
    assert bilinear_interpolation([[0, 64], [128, 255]], 1, 1) == 255
    assert bilinear_interpolation([[0, 64], [128, 255]], 0.5, 0.5) == 112
    assert bilinear_interpolation([[0, 64], [128, 255]], 0.5, 1.5) == 160
    assert bilinear_interpolation([[0, 64, 128], [0, 128, 255], [100, 100, 100]], 2, 2) == 100


def test_apply_kernel():
    assert apply_kernel([[0, 128, 255]], blur_kernel(3)) == [[14, 128, 241]]
    assert apply_kernel([[255, 255, 255]], blur_kernel(3)) == [[255, 255, 255]]
    assert apply_kernel([[0, 128, 255],
                         [0, 128, 255],
                         [0, 128, 255]], blur_kernel(3)) == [[28, 128, 227], [43, 128, 213], [28, 128, 227]]
    assert apply_kernel([[0]], blur_kernel(3)) == [[0]]


def test_get_edges():
    assert get_edges([[200, 50, 200]], 3, 3, 10) == [[255, 0, 255]]
    assert get_edges([[200, 50, 200]], 5, 5, 10) == [[255, 0, 255]]
    assert get_edges([[200, 50, 200]], 1, 1, 10) == [[255, 255, 255]]
    assert get_edges([[200, 50, 200], [200, 50, 200]], 3, 3, 10) == [[255, 0, 255], [255, 0, 255]]
    assert get_edges([[200, 50, 200], [200, 50, 200]], 5, 5, 10) == [[255, 0, 255], [255, 0, 255]]
    assert get_edges([[200, 50, 200]], 3, 3, 10) == [[255, 0, 255]]
    assert get_edges([[]], 3, 3, 10) == [[]]
    assert get_edges([[200]], 3, 3, 10) == [[255]]


def test_quantize():
    assert quantize([[0, 50, 100], [150, 200, 250]], 8) == [[0, 32, 96], [128, 191, 223]]
    assert quantize([[0, 50, 100]], 8) == [[0, 32, 96]]
    assert quantize([[0], [0], [0]], 8) == [[0], [0], [0]]
    assert quantize([[0, 50, 100], [150, 200, 250]],8) == [[0, 32, 96], [128, 191, 223]]


def test_quantize_colored_image():
    assert quantize_colored_image([[[0, 50, 100], [150, 200, 250]]], 8) == [[[0, 32, 96], [128, 191, 223]]]
    assert quantize_colored_image([[[0, 250], [50, 200], [100, 150]], [[150, 100], [200, 50], [250, 0]]],8) \
           == [[[0, 223], [32, 191], [96, 128]], [[128, 96], [191, 32], [223, 0]]]


def test_add_mask():
    assert add_mask([[50, 50, 50]], [[200, 200, 200]], [[0, 0.5, 1]]) == [[200, 125, 50]]


def test_resize():
    assert resize([[0, 64, 128], [0, 128, 255], [100, 100, 100]],2,2) == [[0, 128], [100, 100]]

def main():
    test_seperate_channels()
    test_rotate_90()
    test_combine_channels()
    test_RGB2grayscale()
    test_bilinear_interpolation()
    test_apply_kernel()
    test_get_edges()
    test_quantize()
    test_quantize_colored_image()
    test_add_mask()
    test_resize()


if __name__ == '__main__':
    main()
