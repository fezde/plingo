from plingo import Plingo
from copy import deepcopy


def test_zero():
    lingo = Plingo()

    input = [
        [[18, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[36, 0, 0], [0, 0, 0], [0, 0, 0]],
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
        [[18, 1, 1], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 5, 9], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[18, 6, 10], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 5, 9], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    input = [
        [[18, 4, 1], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 5, 9], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[18, 9, 10], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 5, 9], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    input = [
        [[18, 1, 2], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 5, 9], [0, 0, 0]],
        [[0, 0, 0], [0, 12, 22], [0, 0, 0]],
    ]

    expected = [
        [[18, 13, 24], [0, 0, 0], [0, 0, 0]],
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
        [[18, 10, 10], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 255, 255], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[18, 255, 255], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 255, 255], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    input = [
        [[18, 10, 10], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [255, 255, 255], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[255, 255, 255], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [255, 255, 255], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected
