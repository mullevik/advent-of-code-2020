"""
Day Fifteen - Default dict I guess?
"""
from collections import defaultdict

import utils


if __name__ == '__main__':

    starting_numbers = [int(x) for x in
                        utils.read_strings_from_lines("in/day_15.txt")[0].split(",")]

    memory = defaultdict(lambda: [])

    numbers_spoken = []

    for i, number in enumerate(starting_numbers):

        memory[number].append(i)
        numbers_spoken.append(number)

    iteration = len(numbers_spoken) - 1
    while iteration < (30000000 - 1):

        last_number_spoken = numbers_spoken[iteration]

        last_number_spoken_history = memory[last_number_spoken]
        times_spoken = len(last_number_spoken_history)

        if times_spoken <= 1:

            new_spoken_number = 0

            numbers_spoken.append(new_spoken_number)
            memory[new_spoken_number].append(iteration + 1)

        else:
            a = last_number_spoken_history[-2]
            b = last_number_spoken_history[-1]
            new_spoken_number = b - a

            numbers_spoken.append(new_spoken_number)
            memory[new_spoken_number].append(iteration + 1)

        iteration += 1
        if iteration % 1000 == 0:
            print(iteration)

    print(numbers_spoken[-1])












