"""
Day Twelve - 2D rotations around origin
"""
import math

import utils

from utils import Cords


def clockwise_turn(dir: Cords) -> Cords:
    if dir == (1, 0):
        return Cords(0, -1)
    elif dir == (0, -1):
        return Cords(-1, 0)
    elif dir == (-1, 0):
        return Cords(0, 1)
    elif dir == (0, 1):
        return Cords(1, 0)
    raise ValueError


def counterclockwise_turn(dir: Cords) -> Cords:
    return clockwise_turn(clockwise_turn(clockwise_turn(dir)))


def counter_clockwise_rotate(origin: Cords, point: Cords,
                             degree_angle: int) -> Cords:
    angle = math.radians(degree_angle)

    dy = point.y - origin.y
    dx = point.x - origin.x
    qx = origin.x + int(math.cos(angle)) * dx - int(math.sin(angle)) * dy
    qy = origin.y + int(math.sin(angle)) * dx + int(math.cos(angle)) * dy
    return Cords(qx, qy)


def clockwise_rotate(origin: Cords, point: Cords, degree_angle: int) -> Cords:
    new_angle = 360 - degree_angle
    return counter_clockwise_rotate(origin, point, new_angle)


if __name__ == '__main__':

    lines = utils.read_strings_from_lines("in/day_12.txt")

    position = Cords(0, 0)
    waypoint = Cords(10, 1)
    direction = Cords(1, 0)

    for line in lines:
        print(line)
        print("pos", position)
        print("dir", direction)
        instruction = line[0]
        amount = int(line[1:])

        if instruction == "F":
            difference = waypoint - position
            position += difference * amount
            waypoint += difference * amount

        elif instruction == "N":
            waypoint += Cords(0, amount)

        elif instruction == "S":
            waypoint += Cords(0, -amount)

        elif instruction == "W":
            waypoint += Cords(-amount, 0)

        elif instruction == "E":
            waypoint += Cords(amount, 0)

        elif instruction == "R":
            waypoint = clockwise_rotate(position, waypoint, amount)

        elif instruction == "L":
            waypoint = counter_clockwise_rotate(position, waypoint, amount)

    print("position", position)
    print("direction", direction)

    print("manhattan", abs(position.x) + abs(position.y))
