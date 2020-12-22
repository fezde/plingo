from copy import deepcopy

from plingo import Plingo


def test_zero():
    lingo = Plingo()

    input = [
        [[19, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[38, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected


def test_simple():
    lingo = Plingo()

    input = [
        [[19, 1, 1], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 5, 9], [0, 0, 0]],
        [[0, 0, 0], [0, 7, 8], [0, 0, 0]],
    ]

    expected = [
        [[19, 8, 9], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 5, 9], [0, 0, 0]],
        [[0, 0, 0], [0, 7, 8], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    input = [
        [[19, 4, 1], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 5, 9], [0, 0, 0]],
        [[0, 0, 0], [0, 7, 8], [0, 0, 0]],
    ]

    expected = [
        [[19, 11, 9], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 5, 9], [0, 0, 0]],
        [[0, 0, 0], [0, 7, 8], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    input = [
        [[19, 1, 2], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 5, 9], [0, 0, 0]],
        [[0, 0, 0], [0, 12, 22], [0, 0, 0]],
    ]

    expected = [
        [[19, 6, 11], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 5, 9], [0, 0, 0]],
        [[0, 0, 0], [0, 12, 22], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected


def test_saturation():
    lingo = Plingo()

    input = [
        [[19, 10, 10], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 250, 250], [0, 0, 0]],
    ]

    expected = [
        [[19, 255, 255], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 250, 250], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    input = [
        [[19, 10, 10], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [255, 255, 255], [0, 0, 0]],
    ]

    expected = [
        [[255, 255, 255], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [255, 255, 255], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected
