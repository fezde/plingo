from copy import deepcopy

from plingo import Plingo


def test_zero():
    lingo = Plingo()

    input = [
        [[9, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[9, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected


def test_n_0():
    lingo = Plingo()

    input = [
        [[9, 1, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[9, 1, 0], [9, 1, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=2, save_output=False)
    assert lingo._next_image_data == expected


def test_0_n():
    lingo = Plingo()

    input = [
        [[9, 0, 1], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[9, 0, 1], [0, 0, 0]],
        [[9, 0, 1], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    expected = [
        [[9, 0, 1], [0, 0, 0]],
        [[9, 0, 1], [0, 0, 0]],
        [[9, 0, 1], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=2, save_output=False)
    assert lingo._next_image_data == expected

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=2, save_output=False)
    assert lingo._next_image_data == expected

    input = [
        [[9, 0, 2], [0, 0, 0]],
        [[0, 5, 6], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[9, 0, 2], [0, 0, 0]],
        [[0, 5, 6], [0, 0, 0]],
        [[9, 0, 2], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    input = [
        [[9, 0, 3], [0, 0, 0]],
        [[0, 5, 6], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[9, 0, 3], [0, 0, 0]],
        [[0, 5, 6], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    input = [
        [[9, 0, 2], [0, 0, 0]],
        [[0, 5, 6], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[9, 0, 2], [0, 0, 0]],
        [[9, 0, 2], [0, 0, 0]],
        [[9, 0, 2], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=2, save_output=False)
    assert lingo._next_image_data == expected


def test_n_m():
    lingo = Plingo()

    input = [
        [[9, 1, 1], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[9, 1, 1], [0, 0, 0]],
        [[0, 0, 0], [9, 1, 1]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected

    expected = [
        [[9, 1, 1], [0, 0, 0]],
        [[0, 0, 0], [9, 1, 1]],
        [[9, 1, 1], [0, 0, 0]],
    ]
    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=2, save_output=False)
    assert lingo._next_image_data == expected

    expected = [
        [[9, 1, 1], [9, 1, 1]],
        [[0, 0, 0], [9, 1, 1]],
        [[9, 1, 1], [0, 0, 0]],
    ]
    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=3, save_output=False)
    assert lingo._next_image_data == expected

    expected = [
        [[9, 1, 1], [9, 1, 1]],
        [[9, 1, 1], [9, 1, 1]],
        [[9, 1, 1], [0, 0, 0]],
    ]
    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=4, save_output=False)
    assert lingo._next_image_data == expected

    input = [
        [[9, 5, 4], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    expected = [
        [[9, 5, 4], [0, 0, 0]],
        [[0, 0, 0], [9, 5, 4]],
        [[0, 0, 0], [0, 0, 0]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected
