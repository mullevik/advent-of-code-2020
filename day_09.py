"""
Day Nine - Combinations and lots of iterations
"""
import itertools

import utils

if __name__ == '__main__':

    numbers = utils.read_ints_from_lines("in/day_09.txt")

    offset = 25

    for i, number in enumerate(numbers):

        if i < offset:
            # preamble, do nothing
            pass
        else:
            previous_numbers = numbers[i - offset:i]

            valid = False

            for combination in itertools.combinations(previous_numbers, r=2):

                if combination[0] + combination[1] == number:
                    valid = True
                    break

            if not valid:
                print(f"Invalid: {number}")
                # find contiguous set of numbers which sum up to this
                for j in range(i):
                    sum_total = 0
                    for k in range(j, i):
                        sum_total += numbers[k]

                        if sum_total == number:
                            # found the contiguous set
                            smallest = min(numbers[j:k + 1])
                            largest = max(numbers[j:k + 1])

                            print(f"Result: {smallest + largest}")
                        elif sum_total > number:
                            break



