from apple import Apple
from bomb import Bomb
from snake import Snake
from typing import List, Dict, Any

class Board:

    def __init__(self, width: int, height: int, snake: Snake):
        self.board = [[None for _ in range(width)] for _ in range(height)]
        # for i in range(height):
        #     self.board.append([])
        #     for _ in range(width):
        #         self.board[i].append(None)

        self.objects: Dict[Any] = {
                        "apples": [],
                        "bombs": [],
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


    def draw_board(self):
        pass

    def add_apple(self):
        pass

    def add_car(self):
        pass