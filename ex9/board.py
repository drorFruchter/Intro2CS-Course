from copy import deepcopy
from car import Car
from typing import List, Optional

class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        self.board = [['_' for _ in range(7)] for _ in range(7)]
        self.board[self.target_location()[0]].append("_")
        self.cars = {}


    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        board_str = ""
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                board_str += " " + self.board[row][col] + " "
            board_str += "\n"
        return board_str


    # Works
    def cell_list(self):
        """
        This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cell_lst = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                cell_lst.append((row, col))
        return cell_lst


    # Works
    def _check_valid_move(self, car, move: str) -> bool:
        length, row, col, orientation = car[0], car[1][0], car[1][1], car[2]
        if orientation == 0:
            if move == 'r' or move == 'l':
                return False
            elif (row <= 0 and move =='u') or (row+length > 6 and move=='d'):
                return False
            if row+length+1 < len(self.board) and row-1 >= 0:
                if (self.board[row+length+1][col] != '_' and move == 'd') \
                        or (self.board[row-1][col] != '_' and move == 'u'):
                    return False

        elif orientation == 1:
            if move == 'u' or move == 'd':
                return False
            elif (col <= 0 and move =='l') or (col+length > 6 and move=='r'):
                return False
            elif col+length+1 < len(self.board[row]) and col-1 >= 0:
                if (self.board[row][col+length+1] != '_' and move == 'r') \
                        or (self.board[row][col-1] != '_' and move == 'l'):
                    return False

        return True


    # Works
    def possible_moves(self):
        """
        This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        #From the provided example car_config.json file, the return value could be
        #[('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        moves_lst = []
        possible_moves = {'d': "down", 'r': "right", 'u': "up", 'l': "left"}
        for name, car in self.cars.items():
            for movekey, desc in possible_moves.items():
                if self._check_valid_move(car, movekey):
                    moves_lst.append((name, movekey, "Can go " + desc))
        return moves_lst


    # Works
    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return (3,7)


    # Works
    def cell_content(self, coordinate: (int, int)) -> Optional[str]:
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        row, col = coordinate[0], coordinate[1]
        if row > len(self.board)-1 \
            or row < 0 \
            or col > len(self.board[row])-1 \
            or col < 0:
            return None

        if self.board[row][col] != "_":
            return self.board[row][col]
        return None


    # Works
    def _update_board(self) -> None:
        new_board = [['_' for _ in range(7)] for _ in range(7)]
        new_board[self.target_location()[0]].append("_")
        for car_name, car_object in self.cars.items():
            car_cells = car_object.car_coordinates()
            for cell in car_cells:
                new_board[cell[0]][cell[1]] = car_name
        self.board = new_board


    # Works
    def add_car(self, car: Car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        added: bool = True
        car_coordinates: List[(int,int)] = car.car_coordinates()
        board_coordinates: List[(int,int)] = self.cell_list()

        if len(car_coordinates) > len(self.board): # Car too big for board
            return False
        for cell in car_coordinates: # Check if all cells available
            if self.cell_content(cell) or cell not in board_coordinates:
                return False

        self.cars[car.get_name()] = car
        self._update_board()
        return added


    # Works
    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        if name not in self.cars:
            return False
        car = self.cars[name]
        if len(car.car_coordinates()) <= 0 or movekey not in car.possible_moves():
            return False

        req_cells = car.movement_requirements(movekey)
        board_coordinates = self.cell_list()
        for cell in req_cells:
            if self.cell_content(cell) or cell not in board_coordinates:
                return False

        car.move(movekey)
        self._update_board()
        return True
