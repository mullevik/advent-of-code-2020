"""
Day X - Y
"""

import utils

if __name__ == '__main__':

    lines = utils.read_strings_from_lines("in/day_13.txt")

    departure = int(lines[0])

    numbers = [int(x) for x in lines[1].split(",") if x != "x"]

    print(numbers)

    real_departures = []
    for number in numbers:

        times = departure // number

        if times * number == departure:
            print("Exactly: ", number)
        times += 1
        result = times * number
        real_departures.append(result)

    best_bus_line_index = real_departures.index(min(real_departures))

    print(f"Best departure has ID {numbers[best_bus_line_index]}")
    print(f"The departure is at time {real_departures[best_bus_line_index]}")
    print(f"Solution: {numbers[best_bus_line_index] * (real_departures[best_bus_line_index] - departure)}")