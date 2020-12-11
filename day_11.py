"""
Day Eleven - Coordinates and directions
"""
from typing import List

import utils
from utils import Grid2d, Cords


def find_reachable_seats(grid: Grid2d, coordinates: Cords) -> List[Cords]:
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (-1, -1), (-1, 1), (1, -1),
    ]

    output_coordinates = []

    for direction in directions:

        current = coordinates + direction

        while grid.contains(current):

            if grid[current] in ["#", "L"]:
                output_coordinates.append(current)
                break

            current += direction

    return output_coordinates


if __name__ == '__main__':

    lines = utils.read_strings_from_lines("in/day_11.txt")

    g = utils.Grid2d.from_string_lines(lines, default_value=".")


    changes = 1
    while changes != 0:
        changes = 0

        g_next = g.deepcopy()

        for c in g.all_coordinates():

            cell = g[c]
            neighbors = [g[x] for x in find_reachable_seats(g, c)]

            if cell == "L":

                n_occupied = neighbors.count("#")

                if n_occupied == 0:
                    g_next[c] = "#"
                    changes += 1

            if cell == "#":

                n_occupied = neighbors.count("#")

                if n_occupied >= 5:
                    g_next[c] = "L"
                    changes += 1

        g = g_next
        print(g)
        print(f"changes: {changes}")

    n_occupied = g.all_cells().count("#")
    print(n_occupied)