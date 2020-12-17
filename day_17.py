"""
Day Seventeen - Infinite space (3D and 4D)
"""
from typing import NamedTuple, List, Iterable, Dict
from collections import defaultdict

import utils

class Position(NamedTuple):
    x: int
    y: int
    z: int
    w: int


def adjacent_positions(position: Position) -> Iterable[Position]:
    x_lb, x_ub = position.x - 1, position.x + 1
    y_lb, y_ub = position.y - 1, position.y + 1
    z_lb, z_ub = position.z - 1, position.z + 1
    w_lb, w_ub = position.w - 1, position.w + 1

    for x in range(x_lb, x_ub + 1):
        for y in range(y_lb, y_ub + 1):
            for z in range(z_lb, z_ub + 1):
                for w in range(w_lb, w_ub + 1):

                    adjacent = Position(x, y, z, w)

                    if adjacent != position:
                        yield adjacent


def count_active(universe: Dict[Position, str],
                 positions: Iterable[Position]) -> int:
    result = 0
    for position in positions:

        if position in universe and universe[position] == "#":
            result += 1

    return result


def print_universe(universe: Dict[Position, str]):
    min_x = min(universe.keys(), key=lambda p: p.x).x
    max_x = max(universe.keys(), key=lambda p: p.x).x
    min_y = min(universe.keys(), key=lambda p: p.y).y
    max_y = max(universe.keys(), key=lambda p: p.y).y
    min_z = min(universe.keys(), key=lambda p: p.z).z

    print("Universe")

    for z in range(min_z, max_z + 1):

        print(f"z={z}")

        for y in range(min_y, max_y + 1):
            row = ""
            for x in range(min_x, max_x + 1):
                row += universe[Position(x, y, z)]
            print(row)


if __name__ == '__main__':

    lines = utils.read_strings_from_lines("in/day_17.txt")

    universe = {}

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            p = Position(x, y, 0, 0)

            universe[p] = char

    for i in range(6):
        print(f"Cycle: {i}")
        # print_universe(universe)

        update = {}

        min_x = min(universe.keys(), key=lambda p: p.x).x
        max_x = max(universe.keys(), key=lambda p: p.x).x
        min_y = min(universe.keys(), key=lambda p: p.y).y
        max_y = max(universe.keys(), key=lambda p: p.y).y
        min_z = min(universe.keys(), key=lambda p: p.z).z
        max_z = max(universe.keys(), key=lambda p: p.z).z
        min_w = min(universe.keys(), key=lambda p: p.w).w
        max_w = max(universe.keys(), key=lambda p: p.w).w
        for w in range(min_w - 1, max_w + 2):
            for z in range(min_z - 1, max_z + 2):
                for y in range(min_y - 1, max_y + 2):
                    for x in range(min_x - 1, max_x + 2):

                        position = Position(x, y, z, w)
                        if position not in universe:
                            universe[position] = "."

                        state = universe[position]

                        neighbors = adjacent_positions(position)

                        if state == "#":
                            n_active = count_active(universe, neighbors)

                            if n_active not in (2, 3):
                                update[position] = "."

                        elif state == ".":
                            n_active = count_active(universe, neighbors)

                            if n_active == 3:
                                update[position] = "#"

                        else:
                            raise NotImplementedError

        for position, state in update.items():
            universe[position] = state

    print(count_active(universe, universe.keys()))
