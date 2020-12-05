import warnings
from typing import List, NamedTuple, Any
import itertools


def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def read_ints_from_lines(file="input.txt"):
    with open(file, "r") as f:
        numbers = []
        for x in f.readlines():
            try:
                numbers.append(int(x))
            except ValueError:
                warnings.warn(f"Can not parse int from '{x}'")
        return numbers


def read_floats_from_lines(file="input.txt"):
    with open(file, "r") as f:
        numbers = []
        for x in f.readlines():
            try:
                numbers.append(float(x))
            except ValueError:
                warnings.warn(f"Can not parse float from '{x}'")
        return numbers


def read_strings_from_lines(file="input.txt", strip=True):
    with open(file, "r") as f:
        lines = [x for x in f.readlines()]
        if strip:
            return [x.strip() for x in lines if x.strip() != ""]
        return [x for x in lines]


class Cords(NamedTuple):
    x: int
    y: int


class Grid2d:

    @staticmethod
    def from_string_lines(lines: List[str],
                          default_value: Any = ".") -> 'Grid2d':
        h = len(lines)
        w = len(lines[0])
        tm = Grid2d(w, h, default_value)

        for y, row in enumerate(lines):
            for x, char in enumerate(row):
                tm[x, y] = char

        return tm

    def __init__(self, w: int, h: int, default_value: Any):
        self.width = w
        self.height = h
        self.array = [[default_value for _ in range(w)] for _ in range(h)]

    def contains(self, c: Cords) -> bool:
        x, y = c
        return 0 <= x < self.width and 0 <= y < self.height

    def __setitem__(self, key: Cords, value: Any) -> 'Grid2d':
        assert isinstance(key, tuple)
        x, y = key
        self.array[y][x] = value
        return self

    def __getitem__(self, item: Cords) -> str:
        assert isinstance(item, tuple)
        x, y = item
        return self.array[y][x]


class TreeMap:
    CELL_EMPTY: str = "."
    CELL_TREE: str = "#"


def _test_read_ints_from_lines():
    numbers = read_ints_from_lines(file="test_inputs/ints.txt")
    assert len(numbers) == 4
    assert numbers[0] == 12
    assert numbers[1] == 123
    assert numbers[2] == 66
    assert numbers[3] == 50


def _test_read_floats_from_lines():
    numbers = read_floats_from_lines(file="test_inputs/floats.txt")
    assert len(numbers) == 4
    assert numbers[0] == 12.3
    assert numbers[1] == 123.12
    assert numbers[2] == 66.32
    assert numbers[3] == 50.1


def _test_read_strings_from_lines():
    strings = read_strings_from_lines(file="test_inputs/strings.txt")
    assert len(strings) == 3
    assert strings[0] == "hello"
    assert strings[1] == "\"world\""
    assert strings[2] == "what's up"
    strings = read_strings_from_lines(file="test_inputs/strings.txt",
                                      strip=False)
    assert len(strings) == 6


def _test_grid_2d():
    lines = read_strings_from_lines("test_inputs/tree_map.txt")
    tm = Grid2d.from_string_lines(lines)
    assert tm.height == 3
    assert tm.width == 4
    assert tm[0, 0] == TreeMap.CELL_EMPTY
    assert tm[1, 0] == TreeMap.CELL_TREE
    assert tm[2, 2] == TreeMap.CELL_TREE
    tm[2, 2] = TreeMap.CELL_EMPTY
    assert tm[2, 2] == TreeMap.CELL_EMPTY

    c1 = Cords(2, 2)
    assert tm[c1] == TreeMap.CELL_EMPTY
    tm[c1] = TreeMap.CELL_TREE
    assert tm[c1] == TreeMap.CELL_TREE
    assert tm.contains(c1)
    assert not tm.contains((4, 2))


if __name__ == '__main__':
    _test_read_ints_from_lines()
    _test_read_floats_from_lines()
    _test_read_strings_from_lines()

    _test_grid_2d()
