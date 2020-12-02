"""
Day One - Combinations
"""
import itertools

import utils


if __name__ == '__main__':

    numbers = utils.read_ints_from_lines("in/day_01.txt")

    [print(x * y * z)
     for x, y, z in itertools.combinations(numbers, r=3)
     if x + y + z == 2020]

