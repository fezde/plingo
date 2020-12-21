from copy import deepcopy

from plingo import Plingo


def test_zero():
    lingo = Plingo()

    input = [
        # Row 1
        [[0, 0, 0], [0, 4, 3]],
        # Row 2
        [[0, 1, 1], [0, 2, 2]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 2
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == input

    input = [
        # Row 1
        [[0, 0, 0], [0, 4, 3], [0, 12, 12]],
        # Row 2
        [[0, 1, 1], [0, 2, 2], [0, 12, 13]],
    ]
    lingo._next_image_data = deepcopy(input)
    lingo._height = 2
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == input


def test_iterations():
    lingo = Plingo()

    input = [
        # Row 1
        [[0, 0, 0], [0, 4, 3]],
        # Row 1
        [[0, 1, 1], [0, 2, 2]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 2
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == input

    input = [
        # Row 1
        [[0, 0, 0], [0, 4, 3], [0, 12, 12]],
        # Row 2
        [[0, 1, 1], [0, 2, 2], [0, 12, 13]],
    ]
    lingo._next_image_data = deepcopy(input)
    lingo._height = 2
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=4, save_output=False)
    assert lingo._next_image_data == input


def test_modulo_call():
    lingo = Plingo()

    input = [
        # Row 1
        [
            [len(lingo._command_names), 0, 0],
            [len(lingo._command_names), 4, 3],
            [len(lingo._command_names), 12, 12],
        ],
        # Row 2
        [
            [4 * len(lingo._command_names), 1, 1],
            [3 * len(lingo._command_names), 2, 2],
            [2 * len(lingo._command_names), 12, 13],
        ],
    ]
    lingo._next_image_data = deepcopy(input)
    lingo._height = 2
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == input
