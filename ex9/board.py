from copy import deepcopy


class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        self.board = [['_' for _ in range(7)] for _ in range(7)]
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
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cell_lst = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                cell_lst.append((row, col))
        cell_lst.append((3, 7))
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
        """ This function returns the legal moves of all cars in this board
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


    # Works (Also not a clear function)
    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return (3,7)


    # Works
    def cell_content(self, coordinate):
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
    def _validate_car_input(self, name, length,
                                    location, orientation):
        row, col = location[0], location[1]
        # if (name not in ['Y', 'B', 'O', 'W', 'G', 'R']) \
        if len(name) == 0 \
                or length > 4 \
                or length < 2 \
                or row < 0 \
                or row > 6 \
                or col < 0 \
                or col > 6 \
                or (orientation != 0 and orientation != 1) \
                or (orientation == 0 and row+length > 7) \
                or (orientation == 1 and col+length > 7):
            return False
        return True


    # Works
    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        added: bool = True
        board_copy = deepcopy(self.board)
        if self._validate_car_input(car.name, car.length,
                                    car.location, car.orientation):
            row, col = car.location[0], car.location[1]
            for i in range(car.length):
                if car.orientation == 0:
                    if board_copy[i + row][col] == '_':
                        board_copy[i + row][col] = car.name
                    else:
                        added = False
                        break

                elif car.orientation == 1:
                    if board_copy[row][i+col] == '_':
                        board_copy[row][i+col] = car.name
                    else:
                        added = False
                        break

            if added:
                self.cars[car.name] = [car.length,
                                             [row,col],
                                             car.orientation]
                self.board = board_copy
        else:
            print("The car cannot be added to the board")
            added = False
        return added


    # Works
    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        is_moved: bool = False
        if name not in self.cars:
            print("Car not exist on the board")
            return False

        car = self.cars[name]
        if self._check_valid_move(car, movekey):
            is_moved = True
            length, row, col, orientation = car[0], car[1][0],\
                                            car[1][1], car[2]
            if movekey == 'd' and orientation == 0:
                self.board[row][col] = "_"
                self.board[row+length][col] = name
                car[1][0] += 1

            elif movekey == 'u' and orientation == 0:
                self.board[row+length-1][col] = "_"
                self.board[row-1][col] = name
                car[1][0] -= 1

            elif movekey == 'r' and orientation == 1:
                self.board[row][col] = "_"
                self.board[row][col+length] = name
                car[1][1] += 1

            elif movekey == 'l' and orientation == 1:
                self.board[row][col+length-1] = "_"
                self.board[row][col-1] = name
                car[1][1] -= 1
        if not is_moved:
            print("The car cannot go this way")
        return is_moved
