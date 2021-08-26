from homework7.task2.tic_tac_toe.tic_tac_toe import tic_tac_toe_checker


def test_x_wins():

    board = [["x", "x", "-"], ["-", "x", "o"], ["o", "o", "x"]]

    expected = "x wins!"

    actual = tic_tac_toe_checker(board)

    assert actual == expected


def test_o_wins():
    board = [["x", "o", "-"], ["-", "o", "o"], ["o", "o", "x"]]

    expected = "o wins!"

    actual = tic_tac_toe_checker(board)

    assert actual == expected


def test_draw():
    board = [["x", "x", "x"], ["-", "-", "-"], ["o", "o", "o"]]

    expected = "draw!"

    actual = tic_tac_toe_checker(board)

    assert actual == expected


def test_unfinished():
    board = [["x", "x", "-"], ["-", "x", "o"], ["o", "o", "-"]]

    expected = "unfinished!"

    actual = tic_tac_toe_checker(board)

    assert actual == expected
