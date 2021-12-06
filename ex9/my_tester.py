from board import Board
from car import Car


board = Board()
car1 = Car("R", 2, (3,3), 1)
car2 = Car("B", 3, (4,6), 0)
board.add_car(car1)
board.add_car(car2)
print(board.possible_moves())
print(board.move_car("ddd", "ddd"))
print(board.cars)
print(board)