#################################################################
# FILE : game.py
# WRITER : eyal , eyalmutzary , 206910432
# EXERCISE : intro2cs ex9 2021
# DESCRIPTION: Game class
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################
from board import Board
from car import Car
from helper import load_json
from sys import argv
from copy import deepcopy


class Game:
    """
    A class used for the game of cars. it uses the classes "board" and "car".
    The goal in the game is to get one of the car to the target point, by
    moving one of them at a time
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__board = board

    def __single_turn(self):
        pass

    def _validate_player_input(self, play_st: str) -> bool:
        """
        validates the user's input is in the correct form.
        example: "O,r" - means car_name 'O' move 'r' right.
        :param play_st: player's input
        :return: bool, is it valid?
        """
        if len(play_st) != 3 \
                or play_st[0] not in ['Y', 'B', 'O', 'W', 'G', 'R'] \
                or play_st[1] != ',' \
                or play_st[2] not in ['u', 'd', 'l', 'r']:
            return False
        return True

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        original_board = deepcopy(self.__board)
        print(self.__board)
        play_st = input("Please enter color and direction:")
        while play_st != '!' \
                and not self.__board.cell_content(self.__board.target_location()):
            if self._validate_player_input(play_st):
                car_name, movekey = play_st.split(',')
                if self.__board.move_car(car_name, movekey):
                    print(self.__board)
                else:
                    print("invalid move")
            else:
                print("invalid input")
            if not self.__board.cell_content(self.__board.target_location()):
                play_st = input("Please enter color and direction:")
        print("* GAME OVER *")
        self.__board = original_board


def valid_car_to_game(car: Car, orientation) -> bool:
    """
    validates the car fits to the game rules
    :param car: a Car object
    :return: bool, is it a valid car?
    """
    car_length = len(car.car_coordinates())
    if (car.get_name() not in ['Y', 'B', 'O', 'W', 'G', 'R']) \
            or car_length > 4 \
            or car_length < 2 \
            or (orientation != 0 and orientation != 1):
        return False
    return True


def main() -> None:
    """
    A main function to init load the config file,
    create a board and add the cars to the board.
    """
    cars_api = load_json(argv[1])
    board = Board()
    for car_name, car_details in cars_api.items():
        new_car = Car(car_name,
                      car_details[0],
                      (car_details[1][0], car_details[1][1]),
                      car_details[2])
        if valid_car_to_game(new_car, car_details[2]):
            board.add_car(new_car)
    print(board)
    game = Game(board)
    game.play()


if __name__== "__main__":
    main()
