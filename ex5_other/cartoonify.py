from typing import List
from copy import deepcopy
from math import floor, sqrt
from sys import argv
import ex5_helper

# tested
def separate_channels(image: List[List[List[int]]]):
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


#tested
def combine_channels(channels: List[List[List[int]]]):
    if channels == [[[]]]:
        return channels
    new_image: List[List[List[int]]] = []
    new_image.append([])
    channel_counter = 0
    for row in range(len(channels[channel_counter])):
        if row >= 1:
            new_image.append([])
        for pixel in range(len(channels[channel_counter][row])):
            if len(new_image[row]) < len(channels[channel_counter][row]):
                new_image[row].append([]) # creates a new pixel in the channel
            for i in range(len(channels)):
                new_image[row][pixel].append(channels[i][row][pixel])
        channel_counter += 1
    return new_image


# tested
def RGB2grayscale(colored_image: List[List[List[int]]]):
    new_image: List[List[int]] = []
    for i in range(len(colored_image)):
        new_image.append([])
        for j in range(len(colored_image[i])):
            red: float = colored_image[i][j][0]
            green: float = colored_image[i][j][1]
            blue: float = colored_image[i][j][2]
            new_image[i].append(round(red*0.299 + green*0.587 + blue*0.114))
    return new_image


# works
def blur_kernel(size: int):
    result: List[List[int]] = []
    for _ in range(size):
        inner_list = []
        for _ in range(size):
            inner_list.append(1 / (size**2))
        result.append(inner_list)
    return result


# works
def add_frame_to_image(image: List[List[int]], frame_val: int, k: int):
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


# works
def get_pixel_area(image: List[List[int]], row: int, col: int, k: int):
    framed_image = deepcopy(add_frame_to_image(image, image[row][col], k))
    pixel_area: List[List[int]] = []
    if k > 1:
        row, col = row + int(((k-1)/2)+1), col + int(((k-1)/2))
        radius = int((k-1)/2)
    else:
        radius = 1
    i: int = row - radius - 1
    while i < row+radius:
        pixel_area.append(framed_image[i][col-radius:col+radius +1])
        i += 1
    return pixel_area


# works
def sum_matrix(matrix: List[List[int]]):
    total_sum: int = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            total_sum += matrix[row][col]
    return total_sum


# works
def apply_kernel_on_pixel(image, row, col, k):
    pixel = round(sum_matrix(get_pixel_area(image, row, col, k)) * (1/(k**2)))
    if pixel > 255:
        pixel = 255
    elif pixel < 0:
        pixel = 0
    return pixel


# tested
def apply_kernel(image, kernel):
    k = sqrt(kernel[0][0]**-1)
    if k == 1:
        return image
    blurred_image = deepcopy(image)
    for row in range(len(image)):
        for col in range(len(image[row])):
            blurred_image[row][col] = apply_kernel_on_pixel(image,row,col,k)
    return blurred_image


# works - connected to bilinear_interpolation
def check_xy_valid(y: float, x: float):
    if x > 1:
        x = 1
    elif x < 0:
        x = 0
    if y > 1:
        y = 1
    elif y < 0:
        y = 0
    return y,x


# More tests needed
def bilinear_interpolation(image: List[List[int]], y: float, x: float):
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

    if y == len(image) - 1:
        image.append(image[y])
    if x == len(image[y]) - 1:
        image[y].append(image[y][x])
        image[y+1].append(image[y+1][x])

    calc = round(image[y][x]*(1-a)*(1-b)
                 + image[y+1][x]*a*(1-b)
                 + image[y][x+1]*b*(1-a)
                 + image[y+1][x+1]*a*b)
    return calc


# didn't understand the question
def resize(image, new_height, new_width):
    height_ratio: float = float(new_height / len(image))
    width_ratio: float = float(new_width / len(image[0]))



# tested
def rotate_90(image: List[List[int]], direction: str):
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


# works
def calc_threshold(image: List[List[int]], row: int, col: int, k: int):
    if k > 1:
        pixel_area = get_pixel_area(image, row, col, k)
    else:
        return image[row][col] / (k**2)
    threshold: int = sum_matrix(pixel_area) / (k**2)
    return threshold


# tested
def get_edges(image: List[List[int]], blur_size:int , block_size: int, c:int):
    blurred_image = apply_kernel(image, blur_kernel(blur_size))
    edged_image: List[List[int]] = []
    for row in range(len(image)):
        edged_image.append([])
        for pixel in range(len(blurred_image[row])):
            threshold = calc_threshold(blurred_image, row, pixel, block_size)
            if blurred_image[row][pixel] < threshold - c:
                edged_image[row].append(0)
            else:
                edged_image[row]. append(255)
    return edged_image


# tested
def quantize(image: List[List[int]], N: int):
    new_channel: List[List[int]] = deepcopy(image)
    for row in range(len(new_channel)):
        for col in range(len(new_channel[row])):
            new_channel[row][col] = \
                round(floor(new_channel[row][col] * N/255) * 255/N)
    return new_channel


# tested
def quantize_colored_image(image, N):
    new_image = deepcopy(image)
    for channel in range(len(new_image)):
        new_image[channel] = quantize(new_image[channel], N)
    return new_image


# works
def mask_pixel(pixel1: int, pixel2: int, mask: int):
    if mask > 1:
        mask = 1
    new_pixel = round(pixel1* mask + pixel2* (1 - mask))
    return new_pixel


# more tests needed
def add_mask(image1, image2, mask):
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


"""
seperate to channels
for every channel:
    get edges
    quantize
    add mask of edges
combine channels
"""
def cartoonify(image: List[List[List[int]]],
               blur_size: int,
               th_block_size: int,
               th_c: int,
               quant_num_shades: int):
    new_image = separate_channels(deepcopy(image)) # seperate to channels
    for channel in len(new_image):
        channel_edge = get_edges(new_image[channel], # getting edges
                                 blur_size,
                                 th_block_size,
                                 th_c)
        new_image[channel] = add_mask(new_image[channel], # apply mask on image
                                      channel_edge,
                                      channel_edge)
    new_image = quantize_colored_image(combine_channels(new_image), # quantize
                                       quant_num_shades)
    return new_image

# python3 cartoonify.py <image_source> <cartoon_dest> <max_im_size>
# <blur_size> <th_block_size> <th_c> <quant_num_shades>
if __name__ == "__main__":
    image_source, \
    cartoon_dest, \
    max_im_size, \
    blur_size, \
    th_block_size, \
    th_c, \
    quant_num_shades = argv[1:]
    image = ex5_helper.load_image(image_source)
    if len(image) > max_im_size:
        ratio: float = float(len(image) / max_im_size)
        resize(image, max_im_size, len(image[0])*ratio)
    elif len(image[0]) > max_im_size:
        ratio: float = float(len(image[0]) / max_im_size)
        resize(image, len(image)*ratio, max_im_size)
    pass


