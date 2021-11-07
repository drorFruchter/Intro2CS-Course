from typing import List


def separate_channels(image: List[List[List[int]]]):
    new_lst = []
    for i in range(len(image)):
        for j in range(len(image[i])):
            for color in image[i][j]:
                new_lst.append([[color]])
    return new_lst


def combine_channels(channels: List[List[List[int]]]):
    new_lst: List[List[List[int]]] = [[[]]]
    for channel in channels:
        new_lst[0][0].append(channel[0][0])
    return new_lst


def RGB2grayscale(colored_image: List[List[List[int]]]):
    new_lst: List[List[int]] = []
    for i in range(len(colored_image)):
        for j in range(len(colored_image[i])):
            red: float = colored_image[i][j][0]
            green: float = colored_image[i][j][1]
            blue: float = colored_image[i][j][2]
            new_lst.append([round(red*0.299 + green*0.587 + blue*0.114)])
    return new_lst


# print(separate_channels(combine_channels([[[1]], [[2]]])))
# print(RGB2grayscale ([[[100, 180, 240],[100, 180, 240]]]))