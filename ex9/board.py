#################################################################
# FILE : board.py
# WRITER : eyal , eyalmutzary , 206910432
# EXERCISE : intro2cs ex9 2021
# DESCRIPTION: Board class
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################
from car import Car
from typing import List, Optional


class Board:
    """
    A class that presents a board ("like a parking lot")
    every empty cell is "_", otherwise it contains the name of the car
    """

    def __init__(self):
        """
            A constructor for the Board class
        """
        self.__board = [['_' for _ in range(7)] for _ in range(7)]
        self.__board[self.target_location()[0]].append("_")
        self.__cars = {}

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        board_str = ""
        for row in range(len(self.__board)):
            for col in range(len(self.__board[row])):
                board_str += " " + self.__board[row][col] + " "
            board_str += "\n"
        return board_str

    def cell_list(self):
        """
        This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cell_lst = []
        for row in range(len(self.__board)):
            for col in range(len(self.__board[row])):
                cell_lst.append((row, col))
        return cell_lst

    def _check_valid_move(self, car: Car, movekey: str) -> bool:
        """
        This function checks if the movekry is valid for the car
        :param car: a car object
        :param movekey: a direction fr the car to move
        :return: is it a valid move?
        """
        if len(car.car_coordinates()) <= 0 \
                or movekey not in car.possible_moves():
            return False

        req_cells = car.movement_requirements(movekey)
        board_coordinates = self.cell_list()
        for cell in req_cells:
            if self.cell_content(cell) or cell not in board_coordinates:
                return False

        return True

    def possible_moves(self):
        """
        This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        moves_lst = []
        possible_moves = {'d': "down", 'r': "right", 'u': "up", 'l': "left"}
        for name, car in self.__cars.items():
            for movekey, desc in possible_moves.items():
                if self._check_valid_move(car, movekey):
                    moves_lst.append((name, movekey, "Can go " + desc))
        return moves_lst

    def target_location(self):
        """
        This function returns the coordinates of the location
        which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return (3,7)

    def cell_content(self, coordinate: (int, int)) -> Optional[str]:
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        row, col = coordinate[0], coordinate[1]
        if row > len(self.__board)-1 \
            or row < 0 \
            or col > len(self.__board[row])-1 \
            or col < 0:
            return None

        if self.__board[row][col] != "_":
            return self.__board[row][col]
        return None

    def _update_board(self) -> None:
        """
        This function is used usually after a new car was
        added or changed its location.
        The function updates the board by the new car locations
        """
        new_board = [['_' for _ in range(7)] for _ in range(7)]
        new_board[self.target_location()[0]].append("_")
        for car_name, car_object in self.__cars.items():
            car_cells = car_object.car_coordinates()
            for cell in car_cells:
                new_board[cell[0]][cell[1]] = car_name
        self.__board = new_board

    def add_car(self, car: Car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        added: bool = True
        car_coordinates: List[(int,int)] = car.car_coordinates()
        board_coordinates: List[(int,int)] = self.cell_list()
        if car.get_name() in self.__cars:
            return False
        if len(car_coordinates) > len(self.__board):
            return False
        for cell in car_coordinates:
            if self.cell_content(cell) or cell not in board_coordinates:
                return False

        self.__cars[car.get_name()] = car
        self._update_board()
        return added

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        if name not in self.__cars:
            return False

        car = self.__cars[name]
        if not self._check_valid_move(car, movekey):
            return False

        car.move(movekey)
        self._update_board()
        return True
