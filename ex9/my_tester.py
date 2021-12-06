from board import Board


# board = Board()
# print(board.target_location())

cars = {"toyota": ["bla", ['y', 'n']]}
car = cars["toyota"]
col, row = car[1][0], car[1][1]
car[1][0] = "N"
print(cars)