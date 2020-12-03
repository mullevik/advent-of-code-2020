"""
Day Three - 2D grid + iteration over grid
"""

import utils


if __name__ == '__main__':

    lines = utils.read_strings_from_lines("in/day_03.txt")

    tm = utils.Grid2d.from_string_lines(lines)

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    result = 1

    for slope in slopes:
        x = 0
        y = 0

        trees_found = 0

        while y < tm.height:

            current = tm[x, y]

            if current == utils.TreeMap.CELL_TREE:
                trees_found += 1

            x = (x + slope[0]) % tm.width
            y += slope[1]

        result *= trees_found

    print(result)

