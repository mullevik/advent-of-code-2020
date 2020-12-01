"""
Day One
"""

import sys
import itertools

if __name__ == '__main__':

    numbers = [int(x) for x in sys.stdin.readlines()]

    [print(x * y * z)
     for x, y, z in itertools.combinations(numbers, r=3)
     if x + y + z == 2020]

