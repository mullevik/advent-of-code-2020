"""
Day 10 - DAG (number of paths in DAG)
"""

import utils

if __name__ == '__main__':

    numbers = utils.read_ints_from_lines("in/day_10.txt")
    max_joltage = max(numbers)

    device_joltage = max_joltage + 3
    numbers.append(device_joltage)

    graph = {number: 0 for number in numbers}

    start = 0
    graph[start] = 1

    total_one_differences = 0
    total_three_diffrences = 0
    total_ways = 1
    way_counter_index = -1

    while start != device_joltage:

        possible_joltages = [number for number in numbers if 0 < (number - start) <= 3]

        ways_to_current = graph[start]

        for possible_joltage in sorted(possible_joltages):
            graph[possible_joltage] += ways_to_current

        min_joltage = min(possible_joltages)

        difference = min_joltage - start

        print(f"Jump from {start} to {min_joltage} by {difference}")

        if difference == 1:
            total_one_differences += 1
        elif difference == 3:
            total_three_diffrences += 1
        else:
            print(f"unknown difference {difference}")

        start = min_joltage

    print(f"One jolt: {total_one_differences}")
    print(f"Three jolt: {total_three_diffrences}")
    print(f"Total ways: {graph[device_joltage]}")
    print(total_three_diffrences * total_one_differences)