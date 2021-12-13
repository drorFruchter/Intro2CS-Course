from queue import Queue
from snake import Snake
from board import Board

# snake = Snake()
# print(snake.snake_coordinates())
# snake.possible_moves()
# snake.move()
# print(snake.snake_coordinates())
# print(snake.grow_by_one())
# print(snake.snake_coordinates())
# print(snake.check_collision())

board = Board(0,0, Snake())
# print(board.cell_list())
print(board.cell_content((0,0)))