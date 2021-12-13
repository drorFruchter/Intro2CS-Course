from apple import Apple
from bomb import Bomb
from snake import Snake
from game_parameters import *
from typing import List, Dict, Any

class Board:

    def __init__(self, width: int, height: int, snake: Snake):
        # self.board = {"Size": {"width": width, "height": height},
        #               "Colors": {"green": [],
        #                          "red": [],
        #                          "orange": [],
        #                          "black":[]},
        #               "Objects": {"apples": [],
        #                           "bombs": [],
        #                           "snake": snake}}

        self.board = [[None for _ in range(width)] for _ in range(height)]
        for i in range(height):
            self.board.append([])
            for _ in range(width):
                self.board[i].append(None)
        self.objects = {"apples": [],
                        "bomb": None,
                        "explosion": None,
                        "snake": snake}

    def cell_list(self):
        cells: List = []
        for y in range(len(self.board)-1, -1, -1):
            for x in range(len(self.board[0])-1, -1, -1):
                cells.append((x, y))
        return cells

    def _convert_co_to_index(self, coordinate: (int, int)) -> (int, int):
        row = len(self.board) - coordinate[1] - 1
        col = coordinate[0]
        return row, col

    def cell_content(self, coordinate: (int, int)):
        row, col = self._convert_co_to_index(coordinate)
        return self.board[row][col]

    def _add_item_board(self, item, coordinate):
        row, col = self._convert_co_to_index(coordinate)
        self.board[row][col] = item

    def draw_board(self):
        for apple in self.objects["apples"]:
            self._add_item_board(apple, apple.get_location())
            # what happened if snake ate apple
        if not self.objects["bombs"]:
            bomb = self.objects["bombs"]
            self._add_item_board(bomb, bomb.get_location())
        # elif not self.objects["bombs"]:
            # explosion_coordinates =
        snake_coordinates = self.objects["snake"].snake_coordinates()
        for coordinate in snake_coordinates:
            self._add_item_board(self.objects["snake"], coordinate)

    def add_apple(self, apple: Apple) -> bool:
        if len(self.objects["apples"]) >= 3:
            return False
        # x, y, score = get_random_apple_data()
        # apple = Apple((x, y), score)
        if not self.cell_content(apple.get_location()):
            return False
        else:
            self.objects["apple"].append(apple)

    def add_bomb(self, bomb: Bomb):
        if not self.objects["bombs"] or not self.objects["explosion"]:
            return False
        # x, y, radius, time = get_random_bomb_data()
        # bomb = Bomb((x,y), radius, time)
        if not self.cell_content(bomb.get_location()):
            return False
        else:
            self.objects["bomb"] = bomb