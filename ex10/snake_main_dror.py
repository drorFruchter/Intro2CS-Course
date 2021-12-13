import game_parameters
from game_display import GameDisplay
from board import Board
from snake import Snake
from bomb import Bomb
from apple import Apple

def main_loop(gd: GameDisplay) -> None:
    gd.show_score(0)
    x, y = 10, 10
    while True:
        key_clicked = gd.get_key_clicked()
        if (key_clicked == 'Left') and (x > 0):
            x -= 1
        elif (key_clicked == 'Right') and (x < game_parameters.WIDTH):
            x += 1
        gd.draw_cell(x, y, "red")
        gd.end_round()


def create_board_for_start(board: Board, snake: Snake, bomb: Bomb, apples: [Apple]):



if __name__ == '__main__':
    """
    TODO:
    1: restart the board
    place the snake(starting at 10,10)
    place the bomb
    place the apples
    end_round
    2: every round
    input - key clicked
    moving snake
    checking if :   A. snake crushed on himself - LOSE AND EXIT
                    B. snake crushed on a bomb  - LOSE AND EXIT
                    C. if snake ate bomb - START HIS GROWING PROCESS AND SCORE UPDATE
                    D. bomb exploding - MOVING THE EXPLOSION COORDINATES
                    E. if the explosion hits apple or the snake - UPDATE ACCORDINGLY
    complete apples/ bomb
    draw updated board
    end_round              
    """