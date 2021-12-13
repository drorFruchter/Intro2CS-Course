from queue import Queue
from snake import Snake

snake = Snake()
print(snake.snake_coordinates())
snake.possible_moves()
snake.move()
print(snake.snake_coordinates())
print(snake.grow_by_one())
print(snake.snake_coordinates())
print(snake.check_collision())