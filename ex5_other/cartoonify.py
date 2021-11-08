from typing import List

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


def blur_kernel(size: int):
    result: List[List[int]] = []
    for _ in range(size):
        inner_list = []
        for _ in range(size):
            inner_list.append(1 / (size**2))
        result.append(inner_list)
    return result


# Didn't understand the question
def apply_kernel(image, kernel):
    pass


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


def bilinear_interpolation(image: List[List[int]], y: float, x: float):
    y, x = check_xy_valid(y, x)
    calc = round(image[0][0]*(1-x)*(1-y) + image[1][0]*y*(1-x) + image[0][1]*x*(1-y) + image[1][1]*x*y)
    return calc


# Didn't understand the question
def resize(image, new_height, new_width):
    pass

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


def get_edges(image, blur_size, block_size, c):
    pass


