from copy import deepcopy

from plingo import Plingo


def test_zero():
    lingo = Plingo()

    input = [
        [[15, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[15, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected


def test_simple():
    lingo = Plingo()

    input = [
        [[15, 1, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[0, 0, 0], [15, 1, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected


def test_longer():
    lingo = Plingo()

    input = [
        [[15, 1, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [15, 1, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 5
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    expected = [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [15, 1, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 5
    lingo.execute(show_progressbar=False, iterations=2, save_output=False)
    assert lingo._next_image_data == expected
