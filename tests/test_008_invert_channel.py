from plingo import Plingo
from copy import deepcopy


def test_simple():
    lingo = Plingo()

    input = [
        [[8, 0, 0], [8, 1, 3]],
        [[8, 2, 55], [8, 3, 2]],
        [[8, 2, 12], [8, 3, 22]],
    ]

    expected = [
        [[247, 0, 0], [8, 254, 3]],
        [[8, 2, 200], [247, 3, 2]],
        [[8, 2, 243], [247, 3, 22]],
    ]

    lingo._next_image_data = deepcopy(input)
    lingo._height = 3
    lingo._width = 2
    lingo.execute(show_progressbar=False, iterations=1, save_output=False)
    assert lingo._next_image_data == expected
