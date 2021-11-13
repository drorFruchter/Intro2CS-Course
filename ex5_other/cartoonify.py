#################################################################
# FILE : cartoonify.py
# WRITER : eyal , eyalmutzary , 206910432
# EXERCISE : intro2cs ex5 2021
# DESCRIPTION: Image proccesing script
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

from typing import List
from copy import deepcopy
from math import floor, sqrt
from sys import argv
import ex5_helper


def separate_channels(image: List[List[List[int]]]):
    """
        Seperates an image to channels
        :param image - an image with 1 or more channels
        :return a list with all channels seperated
    """
    if image == [[[]]]:
        return image
    new_lst: List[List[List[int]]] = []
    for _ in range(len(image[0][0])): # creating channels layer
        new_lst.append([])
    for row in range(len(image)):
        for channel in range(len(image[row][0])): # new row in every channel
            new_lst[channel].append([])
        for col in range(len(image[row])):
            for channel, value in enumerate(image[row][col]):
                new_lst[channel][row].append(value) # adds value by channel
    return new_lst


def combine_channels(channels: List[List[List[int]]]):
    """
        Combines multiple channels to an image
        :param channels - a list of 2D list of channels
        :return an image as a 3D list
    """
    if channels == [[[]]]:
        return [[[]]]
    combined_image = []
    for row in range(len(channels[0])):
        combined_image.append([])
        for col in range(len(channels[0][0])):
            combined_image[row].append([])
            for ch in range(len(channels)):
                combined_image[row][col].append(channels[ch][row][col])
    return combined_image


def RGB2grayscale(colored_image: List[List[List[int]]]):
    """
        Turns RGB channels to a single channel
        :param colored_image - an image to grayscale
        :return a grayscaled image (2D list)
    """
    new_image: List[List[int]] = []
    for i in range(len(colored_image)):
        new_image.append([])
        for j in range(len(colored_image[i])):
            red: float = colored_image[i][j][0]
            green: float = colored_image[i][j][1]
            blue: float = colored_image[i][j][2]
            new_image[i].append(round(red*0.299 + green*0.587 + blue*0.114))
    return new_image


def blur_kernel(size: int):
    """
        creates a 2d list by the blur size
        :param size - blur kernel size
        :return a 2D list of the blur kernel
    """
    result: List[List[int]] = []
    size = int(size)
    for _ in range(size):
        inner_list = []
        for _ in range(size):
            inner_list.append(1 / (size**2))
        result.append(inner_list)
    return result


def add_frame_to_image(image: List[List[int]], frame_val: int, k: int):
    """
        Adds a frame to a 2D list
        :param image - a 2D list
        :param frame_val - the value of the frame elements
        :param k - adds a frame of the size (k-1)//2
        :return a new framed list
    """
    framed_image: List[List[int]] = deepcopy(image)
    for i in range(len(image)):
        for _ in range(2):
            framed_image[i].extend([frame_val]*(floor((k-1)/2)))
            framed_image[i] = framed_image[i][::-1]
    if k > 0:
        top = [frame_val for _ in range(len(framed_image[0]))]
        for _ in range(int((k-1)/2)):
            framed_image = [top] + framed_image + [top]
    return framed_image


def get_pixel_area(image: List[List[int]], row: int, col: int, k: int):
    """
        Picks a pixel in the channel and returns the area around it.
        :param image - a 2D list (channel)
        :param row - the row of the pixel
        :param col - the col of the pixel
        :param k - the length of one size of the square (k*k square)
        :return a 2D list of the square around the pixel
    """
    framed = False
    if k > 1:
        radius = int((k-1)/2)
    else:
        radius = 1

    if row >= len(image)-1-radius \
            or col >= len(image[0])-1-radius \
            or row == 0 \
            or col == 0:
        framed_image = add_frame_to_image(image, image[row][col], k)
        framed = True
    else:
        framed_image = image

    pixel_area: List[List[int]] = []
    if k > 1 and framed:
        row, col = row + int(((k-1)/2)+1), col + int(((k-1)/2))

    i: int = row - radius - 1
    while i < row+radius:
        pixel_area.append(framed_image[i][col-radius:col+radius +1])
        i += 1
    return pixel_area


def sum_matrix(matrix: List[List[int]]):
    """
        Calculate the sum of the elements in the matrix
        :param matrix - a 2D list
        :return the sum of the matrix
    """
    total_sum: int = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            total_sum += matrix[row][col]
    return total_sum


def apply_kernel_on_pixel(image: List[List[int]], row: int, col: int, k: int):
    """
        Applies the kernel on a single pixel
        :param image - a 2D list (channel)
        :param row - the row of the pixel
        :param col - the col of the pixel
        :param k - the length of one size of the square (k*k square)
        :return The new value of the pixel
    """
    pixel = round(sum_matrix(get_pixel_area(image, row, col, k)) * (1/(k**2)))
    if pixel > 255:
        pixel = 255
    elif pixel < 0:
        pixel = 0
    return pixel


def apply_kernel(image: List[List[int]], kernel: List[List[int]]):
    """
        applies a kernel on a channel
        :param image - a 2D list (channel)
        :param kernel - a 2D list of the kernel
        :return a new kerneled channel
    """
    k = sqrt(kernel[0][0]**-1)
    if k == 1:
        return image
    blurred_image = deepcopy(image)
    for row in range(len(image)):
        for col in range(len(image[row])):
            blurred_image[row][col] = apply_kernel_on_pixel(image,row,col,k)
    return blurred_image


def bilinear_interpolation(image: List[List[int]], y: float, x: float):
    """
        Caculate the avg of a pixel between pixels
        :param image - a 2D list (channel)
        :param y - the row of the pixel
        :param x - the col of the pixel
        :return The pixel value
    """
    a, b = y%1, x%1
    y, x = int(y), int(x)

    if y >= len(image):
        y = len(image) - 1
    elif y < 0:
        y = 0
    if x >= len(image[y]):
        x = len(image[y]) - 1
    elif x < 0:
        x = 0
    image_copy = deepcopy(image)
    if y == len(image_copy) - 1:
        image_copy.append(image_copy[y])
    if x == len(image_copy[y]) - 1:
        image_copy[y].append(image_copy[y][x])
        image_copy[y+1].append(image_copy[y+1][x])
    calc = round(image_copy[y][x]*(1-a)*(1-b)
                 + image_copy[y+1][x]*a*(1-b)
                 + image_copy[y][x+1]*b*(1-a)
                 + image_copy[y+1][x+1]*a*b)
    return calc


def resize(image: List[List[int]], new_height: int, new_width: int):
    """
        Resizes a channel by new sizes
        :param image - a 2D list (channel)
        :param new_height - the new height of the image
        :param new_width - the new width of the image
        :return a new resized 2D List
    """
    height_ratio: float = float(len(image) / new_height)
    width_ratio: float = float(len(image[0]) / new_width)
    new_image = []
    new_row_i = 0
    row_skip, col_skip = 0.0, 0.0
    while row_skip < len(image):
        new_image.append([])
        while col_skip < len(image[0]):
            new_image[new_row_i].append(bilinear_interpolation(image, row_skip, col_skip))
            col_skip += width_ratio
        row_skip += height_ratio
        col_skip = 0
        new_row_i += 1
    new_image[0][0] = image[0][0]
    new_image[0][-1] = image[0][-1]
    new_image[-1][0] = image[-1][0]
    new_image[-1][-1] = image[-1][-1]
    return new_image


def resize_image(image: List[List[List[int]]], new_height, new_width):
    """
        Resizes an image by new sizes
        :param image - a 3D list
        :param new_height - the new height of the image
        :param new_width - the new width of the image
        :return a new resized image
    """
    image_copy = deepcopy(image)
    image_copy = separate_channels(image_copy)
    new_image = []
    for channel in range(len(image_copy)):
        new_image.append(resize(channel, new_height, new_width))
    new_image = combine_channels(new_image)
    return new_image


def rotate_90(image: List[List[int]], direction: str):
    """
        Rotates a channel 90 degrees
        :param image - a 2D list (channel)
        :param direction - could be R or L (Right or Left)
        :return a new rotated 2D List
    """
    new_image: List[List[int]] = []
    new_row: List[int] = []
    for i in range(len(image[0])):
        for j in range(len(image), 0, -1):
            new_row.append(image[j-1][i])
        new_image.append(new_row)
        new_row = []
    if direction == 'R':
        return new_image
    elif direction == 'L':
        return [row[::-1] for row in new_image[::-1]]
    return None


def calc_threshold(image: List[List[int]], row: int, col: int, k: int):
    """
        Caculate the threshold for a single pixel
        :param image - a 2D list (channel)
        :param row - the row of the pixel
        :param col - the col of the pixel
        :return the threshold
    """
    k = int(k)
    if k > 1:
        pixel_area = get_pixel_area(image, row, col, k)
    else:
        return image[row][col] / (k**2)
    threshold: int = sum_matrix(pixel_area) / (k**2)
    return threshold


def get_edges(image: List[List[int]], blur_size:int , block_size: int, c:int):
    """
        finds the edges of the channel
        :param image - a 2D list (channel)
        :param blur_size - the amount of blurring
        :param block_size - the size of the block to blur
        :param c - a parameter to adjust the edge detection
        :return a new edged channel
    """
    blurred_image = apply_kernel(image, blur_kernel(blur_size))
    edged_image: List[List[int]] = []
    for row in range(len(image)):
        edged_image.append([])
        for pixel in range(len(blurred_image[row])):
            threshold = calc_threshold(blurred_image, row, pixel, block_size)
            if blurred_image[row][pixel] < threshold - int(c):
                edged_image[row].append(0)
            else:
                edged_image[row]. append(255)
    return edged_image


def quantize(image: List[List[int]], N: int):
    """
        Doing a quantize proccess to a signle channel
        :param image - a 2D list (channel)
        :param N - the amount of colors
        :return a new quantized channel
    """
    new_channel: List[List[int]] = deepcopy(image)
    N = int(N)
    for row in range(len(new_channel)):
        for col in range(len(new_channel[row])):
            new_channel[row][col] = \
                round(floor(new_channel[row][col] * N/255) * 255/N)
    return new_channel


def quantize_colored_image(image: List[List[List[int]]], N:int):
    """
        Going for the quantize process for every channel
        :param image - a 3D list (channel)
        :param N - the amount fo colorss
        :return a new quantized image
    """
    image_copy = deepcopy(image)
    image_copy = separate_channels(image_copy)
    new_image = []
    for channel in range(len(image_copy)):
        new_image.append(quantize(image_copy[channel], N))
    new_image = combine_channels(new_image)
    return new_image


def mask_pixel(pixel1: int, pixel2: int, mask: int):
    """
        masks a single pixel
        :param pixel1 - a pixel value
        :param pixel2 - another pixel value
        :param mask - the mask value
        :return a masked pixel value
    """
    if mask > 1:
        mask = 1
    new_pixel = round(pixel1* mask + pixel2* (1 - mask))
    return new_pixel


def add_mask(image1, image2, mask):
    """
        adds a mask to an image
        :param image1 - a 2D or 3D List
        :param image2 - a 2D or 3D List
        :param mask - a 2D List
        :return a new masked image
    """
    new_image = []
    is_multi_channel = type(image1[0][0]) == type(list())
    for row in range(len(image1)):
        new_image.append([])
        for col in range(len(image1[row])):
            if is_multi_channel:
                for channel in range(len(image1[row][col])):
                    new_image[row].append([])
                    new_image[row][col].append(
                        mask_pixel(image1[row][col][channel],
                                   image2[row][col][channel],
                                   mask[row][col]))
            else:
                new_image[row].append(mask_pixel(image1[row][col],
                                                 image2[row][col],
                                                 mask[row][col]))
    return new_image


def cartoonify(image: List[List[List[int]]],
               blur_size: int,
               th_block_size: int,
               th_c: int,
               quant_num_shades: int):
    """
        Doing the cartoonify effect to an image
        :param image - a 3D List
        :param blur_size - the amount of blurness
        :param th_block_size - size of the block to determine the threshold
        :param th_c - a parameter to reduce when using edge detection
        :param quant_num_shades - amount of shades for quantize
        :return a new cartoonified image
    """
    new_image = separate_channels(deepcopy(image)) # seperate to channels
    for channel in range(len(new_image)):
        channel_edge = get_edges(new_image[channel], # getting edges
                                 blur_size,
                                 th_block_size,
                                 th_c)
        new_image[channel] = add_mask(new_image[channel], # apply mask on image
                                      channel_edge,
                                      channel_edge)
    new_image = combine_channels(new_image)
    new_image = quantize_colored_image(new_image, # quantize
                                       quant_num_shades)
    return new_image


if __name__ == "__main__":
    image_source, \
    cartoon_dest, \
    max_im_size, \
    blur_size, \
    th_block_size, \
    th_c, \
    quant_num_shades = argv[1:]
    image = ex5_helper.load_image(image_source)
    max_im_size = int(max_im_size)
    if len(image) > max_im_size or len(image[0]) > max_im_size:
        if len(image) > len(image[0]):
            ratio: float = float(max_im_size / len(image))
            resize_image(image, max_im_size, len(image[0])*ratio)
        else:
            ratio: float = float(max_im_size / len(image[0]))
            resize_image(image, len(image)*ratio, max_im_size)

    new_image = cartoonify(image, blur_size, th_block_size, th_c, quant_num_shades)
    ex5_helper.save_image(new_image, cartoon_dest)
