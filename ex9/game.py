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


    def _validate_player_input(self, play_st: str):
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
        play_st = input("Please enter color and direction:")
        while play_st != '!' \
                and not self.board.cell_content(self.board.target_location()):
            if self._validate_player_input(play_st):
                car_name, movekey = play_st.split(',')
                if self.board.move_car(car_name, movekey):
                    print(self.board)
                else:
                    print("invalid move")
            else:
                print("invalid input")
            if not self.board.cell_content(self.board.target_location()):
                play_st = input("Please enter color and direction:")
        print("* GAME OVER *")


def valid_car_to_game(car: Car) -> bool:
    car_length = len(car.car_coordinates())
    if (car.get_name() not in ['Y', 'B', 'O', 'W', 'G', 'R']) \
            or car_length > 4 \
            or car_length < 2 \
            or (car.orientation != 0 and car.orientation != 1):
        return False
    return True


def main() -> None:
    cars_api = load_json(argv[1])
    # cars_api = load_json("car_config.json")
    board = Board()
    for car_name, car_details in cars_api.items():
        new_car = Car(car_name,
                      car_details[0],
                      (car_details[1][0], car_details[1][1]),
                      car_details[2])
        if valid_car_to_game(new_car):
            print("Car added")
            board.add_car(new_car)
    print(board)
    game = Game(board)
    game.play()
    print(board)






if __name__== "__main__":
    #Your code here
    #All access to files, non API constructors, and such must be in this
    #section, or in functions called from this section.
    main()
