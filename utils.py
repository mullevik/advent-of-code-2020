import warnings
import copy
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

    def __add__(self, other: Any):
        if isinstance(other, Cords):
            return Cords(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return Cords(self.x + other[0], self.y + other[1])
        elif isinstance(other, int):
            return Cords(self.x + other, self.y + other)
        else:
            raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Cords):
            return Cords(self.x - other.x, self.y - other.y)
        elif isinstance(other, tuple):
            return Cords(self.x - other[0], self.y - other[1])
        else:
            raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, int):
            return Cords(self.x * other, self.y * other)
        else:
            raise NotImplementedError

    def __rmul__(self, other):
        if isinstance(other, int):
            return Cords(self.x * other, self.y * other)
        else:
            raise NotImplementedError


class Grid2d:
    """
    2D grid indexed by (x, y) tuples
    """

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

    def eight_neighborhood(self, c: Cords) -> List[Cords]:

        if not isinstance(c, Cords):
            c = Cords(c[0], c[1])

        x_lb = max(c.x - 1, 0)
        x_ub = min(c.x + 2, self.width)

        y_lb = max(c.y - 1, 0)
        y_ub = min(c.y + 2, self.height)

        neighbors = []

        for x in range(x_lb, x_ub):
            for y in range(y_lb, y_ub):

                if not (x == c.x and y == c.y):
                    neighbors.append(Cords(x=x, y=y))

        return neighbors

    def contains(self, c: Cords) -> bool:
        x, y = c
        return 0 <= x < self.width and 0 <= y < self.height

    def deepcopy(self) -> 'Grid2d':
        g = Grid2d(self.width, self.height, default_value=".")
        new_array = copy.deepcopy(self.array)
        g.array = new_array
        return g

    def all_coordinates(self) -> List[Cords]:
        coordinates = []
        for y in range(self.height):
            for x in range(self.width):
                coordinates.append(Cords(x, y))
        return coordinates

    def all_cells(self) -> List[Any]:
        cells = []
        for y in range(self.height):
            for x in range(self.width):
                cells.append(self[x, y])
        return cells

    def __setitem__(self, key: Cords, value: Any) -> 'Grid2d':
        assert isinstance(key, tuple)
        x, y = key
        self.array[y][x] = value
        return self

    def __getitem__(self, item: Cords) -> str:
        assert isinstance(item, tuple)
        x, y = item
        return self.array[y][x]

    def __str__(self):
        out = ""
        for y in range(self.height):
            for x in range(self.width):
                out += self[x, y]
            out += "\n"
        return out


class TreeMap:
    CELL_EMPTY: str = "."
    CELL_TREE: str = "#"


def decimal_to_bit_list(number: int, bit_len: int) -> List[bool]:
    bits = [False] * bit_len

    for i in range(bit_len):

        divider = 2 ** (bit_len - 1 - i)

        times = number // divider

        if times > 0:
            bits[i] = True

        number = number % divider

    return bits


def bit_list_to_decimal(bit_list: List[int]) -> int:
    accumulator = 0
    for i, bit in enumerate(reversed(bit_list)):
        if bit:
            accumulator += 2 ** i
    return accumulator


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


def _test_bits():

    bit_list = decimal_to_bit_list(11, 36)
    assert len(bit_list) == 36
    assert bit_list[35]
    assert bit_list[34]
    assert not bit_list[33]
    assert bit_list[32]
    assert not bit_list[31]
    assert not bit_list[0]

    assert bit_list_to_decimal([True, False, True, True]) == 11
    assert bit_list_to_decimal([False, True, False, True, True]) == 11


if __name__ == '__main__':
    _test_read_ints_from_lines()
    _test_read_floats_from_lines()
    _test_read_strings_from_lines()

    _test_grid_2d()

    _test_bits()
