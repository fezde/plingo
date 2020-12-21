from copy import deepcopy

from plingo import Plingo


def test_simple():
    lingo = Plingo()

    input = [
        # Row 1
        [[3, 0, 0], [3, 4, 3]],
        # Row 1
        [[3, 1, 0], [0, 2, 2]],
    ]

    expected = [
        # Row 1
        [[252, 255, 255], [252, 251, 252]],
        # Row 1
        [[252, 254, 255], [0, 2, 2]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 2
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected


def test_modulo():
    lingo = Plingo()

    cmds = len(lingo._command_names)

    input = [
        # Row 1
        [[3 + cmds, 0, 0], [3, 4, 3]],
        # Row 1
        [[3, 1, 0], [0, 2, 2]],
    ]

    expected = [
        # Row 1
        [[255 - (3 + cmds), 255, 255], [252, 251, 252]],
        # Row 1
        [[252, 254, 255], [0, 2, 2]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 2
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected
