from apple import Apple
from bomb import Bomb
from snake import Snake
from typing import List

class Board:

    def __init__(self, width: int, height: int, snake: Snake):
        self.board = []
        for i in range(height):
            self.board.append([])
            for _ in range(width):
                self.board[i].append(None)

        self.apples: List[Apple] = []
        self.bombs: List[Bomb] = []
        self.snake: Snake = snake

    def cell_list(self):
        pass

    def cell_content(self, coordinate: (int, int)):
        pass

    def draw_board(self):
        pass

    def add_apple(self):
        pass

    def add_car(self):
        pass