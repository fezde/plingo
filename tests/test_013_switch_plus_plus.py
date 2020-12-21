from copy import deepcopy

from plingo import Plingo


def test_zero():
    lingo = Plingo()

    input = [
        [[13, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[13, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected


def test_switch_vs_other_commands():
    lingo = Plingo()

    input = [
        [[13, 1, 0], [0, 0, 0]],
        [[3, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[0, 0, 0], [13, 1, 0]],
        [[252, 255, 255], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    input = [
        [[13, 0, 1], [0, 0, 0]],
        [[3, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[3, 0, 0], [0, 0, 0]],
        [[252, 255, 255], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    input = [
        [[0, 0, 0], [0, 0, 0]],
        [[3, 0, 0], [0, 0, 0]],
        [[13, 0, 2], [0, 0, 0]],
    ]

    expected = [
        [[0, 0, 0], [0, 0, 0]],
        [[13, 0, 2], [0, 0, 0]],
        [[3, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected
