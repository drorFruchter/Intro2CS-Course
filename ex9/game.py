from board import Board
from car import Car
from helper import load_json
from sys import argv
from typing import List, Union


class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board
        #You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')


    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        pass


    def _validate_car_move(self, car_name: str, move: str) -> bool:
        car = self.board.cars[car_name]
        board = self.board.board
        length, row, col, orientation = car[0], car[1][0], car[1][1], car[2]
        if car_name not in ['Y', 'B', 'O', 'W', 'G', 'R']:
            return False

        if orientation == 0:
            if move == 'r' or move == 'l':
                return False
            elif (row <= 0 and move =='u') or (row+length > 6 and move=='d'):
                return False
            if row+length+1 < len(board) and row-1 >= 0:
                if (board[row+length+1][col] != '_' and move == 'd') \
                        or (board[row-1][col] != '_' and move == 'u'):
                    return False

        elif orientation == 1:
            if move == 'u' or move == 'd':
                return False
            elif (col <= 0 and move =='l') or (col+length > 6 and move=='r'):
                return False
            elif col+length+1 < len(board[row]) and col-1 >= 0:
                if (board[row][col+length+1] != '_' and move == 'r') \
                        or (board[row][col-1] != '_' and move == 'l'):
                    return False

        return True

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # play_st = input("Please enter color and direction:")
        play_st = "O,u"
        print(self.board.cell_content(self.board.target_location()))
        while play_st != '!' \
            and not self.board.cell_content(self.board.target_location()):
            car_name, movekey = play_st.split(',')
            if self._validate_car_move(car_name, movekey):
                print(self.board.move_car(car_name, movekey)) # CAR NOT MOVING
                print(self.board)
            else:
                print("invalid move")
            play_st = input("Please enter color and direction:")






def valid_car_to_game(board: Board,
                      car_name: str,
                      car_details) -> bool:
    length, row, col, orientation = car_details[0], \
                                    car_details[1][0], car_details[1][1], \
                                    car_details[2]
    board_size = len(board.board)
    if (car_name not in ['Y', 'B', 'O', 'W', 'G', 'R']) \
            or len(car_name) == 0 \
            or length > 4 \
            or length < 2 \
            or row < 0 \
            or row > board_size-1\
            or col < 0 \
            or col > board_size-1\
            or (orientation != 0 and orientation != 1) \
            or (orientation == 0 and row+length > board_size) \
            or (orientation == 1 and col+length > board_size):
        return False
    return True


def main() -> None:
    # cars_api = load_json(argv[1])
    cars_api = load_json("car_config.json")
    board = Board()
    for car_name, car_details in cars_api.items():
        if valid_car_to_game(board, car_name, car_details):
            board.add_car(Car(car_name, *car_details))
    print(board)
    game = Game(board)
    game.play()






if __name__== "__main__":
    #Your code here
    #All access to files, non API constructors, and such must be in this
    #section, or in functions called from this section.
    main()
