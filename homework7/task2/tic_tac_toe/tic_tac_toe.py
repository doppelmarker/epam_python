"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def get_win_conditions():
    return [
        # rows
        0b000000111,
        0b000111000,
        0b111000000,
        # columns
        0b100100100,
        0b010010010,
        0b001001001,
        # diagonals
        0b100010001,
        0b001010100,
    ]


def get_board_state(board):
    x_state, o_state = 0, 0
    for i, subarray in enumerate(board):
        for j, element in enumerate(subarray):
            if element == "x":
                x_state += 2 ** (j + i * len(board))
            elif element == "o":
                o_state += 2 ** (j + i * len(board))
    return x_state, o_state


def tic_tac_toe_checker(board: List[List]) -> str:
    x_state, o_state = get_board_state(board)
    x_wins, o_wins = False, False
    win_conditions = get_win_conditions()

    for win_condition in win_conditions:
        if x_state & win_condition == win_condition:
            x_wins = True
        elif o_state & win_condition == win_condition:
            o_wins = True

    if x_wins and o_wins:
        return "draw!"
    elif x_wins:
        return "x wins!"
    elif o_wins:
        return "o wins!"
    else:
        return "unfinished!"
