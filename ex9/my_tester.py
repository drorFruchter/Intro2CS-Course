from board import Board
from car import Car


board = Board()
car1 = Car("R", 2, (3,3), 1)
car2 = Car("B", 3, (4,6), 0)
board.add_car(car1)
board.add_car(car2)
# print(car1.get_name())
print(board.possible_moves())
print(car2.movement_requirements('d'))


# print(board.cars)
print(board)
print(board.cell_list())

# car1 = Car("kkkk", -1, (2,4), 1)
# car2 = Car("B", 3, (4,6), 0)
# print(car1.car_coordinates())
