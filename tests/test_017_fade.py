from plingo import Plingo
from copy import deepcopy


def test_zero():
    lingo = Plingo()

    input = [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [17, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [2, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected


def test_borders():
    lingo = Plingo()

    input = [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [17, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [3, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    input = [
        [[0, 0, 0], [17, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[0, 0, 0], [3, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    input = [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[17, 0, 0], [0, 0, 0], [17, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[3, 0, 0], [0, 0, 0], [3, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected


def test_corners():
    lingo = Plingo()

    input = [
        [[17, 0, 0], [0, 0, 0], [17, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[17, 0, 0], [0, 0, 0], [17, 0, 0]],
    ]

    expected = [
        [[4, 0, 0], [0, 0, 0], [4, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[4, 0, 0], [0, 0, 0], [4, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected


def test_all_channels():
    lingo = Plingo()

    input = input = [
        [[0, 0, 0], [0, 9, 0], [0, 0, 0]],
        [[0, 0, 0], [17, 0, 0], [0, 0, 27]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[0, 0, 0], [0, 9, 0], [0, 0, 0]],
        [[0, 0, 0], [2, 1, 3], [0, 0, 27]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    input = input = [
        [[0, 0, 0], [0, 9, 0], [0, 0, 0]],
        [[0, 9, 0], [17, 0, 0], [0, 0, 27]],
        [[0, 9, 0], [0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[0, 0, 0], [0, 9, 0], [0, 0, 0]],
        [[0, 9, 0], [2, 3, 3], [0, 0, 27]],
        [[0, 9, 0], [0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 3
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected
