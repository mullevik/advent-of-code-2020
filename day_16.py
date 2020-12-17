"""
Day Sixteen - Constraint Satisfaction Problem
"""
import random
from copy import copy, deepcopy
from typing import List, Dict

import utils


def is_one_correct(position: int, field: str, fields: Dict[str, tuple],
                   tickets: List[List[int]]) -> bool:
    for ticket in tickets:

        ranges = fields[field]

        matches = 0
        for r in ranges:
            if r[0] <= ticket[position] <= r[1]:
                matches += 1

        if matches == 0:
            return False

    return True


def is_correct(selection: List[str], fields: Dict[str, tuple],
               tickets: List[List[int]]) -> bool:

    for ticket in tickets:

        for i, value in enumerate(ticket):

            ranges = fields[selection[i]]

            matches = 0
            for r in ranges:
                if r[0] <= value <= r[1]:
                    matches += 1

            if matches == 0:
                return False

    return True


if __name__ == '__main__':

    lines = utils.read_strings_from_lines("in/day_16.txt", strip=False)

    input_index = 0

    fields = {}

    while True:

        current_line = lines[input_index]
        if current_line == "\n":
            break

        field_name = current_line.split(":")[0]
        first_range = current_line.split(":")[1].split()[0]
        second_range = current_line.split(":")[1].split()[2]

        fields[field_name] = set()

        fields[field_name].add((int(first_range.split("-")[0]), int(first_range.split("-")[1])))
        fields[field_name].add((int(second_range.split("-")[0]), int(second_range.split("-")[1])))

        input_index += 1

    print(fields)

    input_index += 2
    owned_ticket_line = lines[input_index]
    print("My ticker", owned_ticket_line)

    tickets = [[int(x) for x in owned_ticket_line.split(",")]]
    ticket_length = len(tickets[0])

    invalid_values = []

    input_index += 3
    while input_index < len(lines):
        values = [int(x) for x in lines[input_index].split(",")]

        valid = True
        for value in values:

            matches = 0
            for the_range in fields.values():
                for r in the_range:
                    if r[0] <= value <= r[1]:
                        matches += 1

            if matches == 0:
                valid = False

        if valid:
            tickets.append(values)

        input_index += 1

    all_options = set(fields.keys())
    tried_options = [set() for _ in range(ticket_length)]
    allowed_options = [set() for _ in range(ticket_length)]
    print(f"Allowed options: {[len(x) for x in allowed_options]}")

    for i in range(ticket_length):
        for option in all_options:
            if is_one_correct(i, option, fields, tickets):
                allowed_options[i].add(option)

    selection = [None] * ticket_length

    # position = 0
    # iterations = 0
    # while True:
    #     iterations += 1
    #     possibilities = allowed_options[position]\
    #         .difference(tried_options[position])\
    #         .difference(set(selection))
    #
    #     if iterations % 50000 == 0:
    #         print(f"Tried options: {[len(x) for x in tried_options]}")
    #
    #     if not possibilities:
    #         # no more possibilities... back track
    #         tried_options[position] = set()
    #         selection[position] = None
    #         position -= 1
    #         continue
    #
    #     picked_field = next(iter(possibilities))
    #     tried_options[position].add(picked_field)
    #
    #     if is_one_correct(position, picked_field, fields, tickets):
    #         # this pick is correct, onto the next one
    #         selection[position] = picked_field
    #         position += 1
    #
    #     if position < 0:
    #         print("Unsolvable")
    #         break
    #
    #     if position >= ticket_length:
    #         print("Hey")
    #         break
    #
    # assert is_correct(selection, fields, tickets)

    # computed by the previous backtracking
    solution = ['train', 'duration', 'row', 'departure station', 'departure date', 'departure time', 'price', 'arrival platform', 'zone', 'wagon', 'seat', 'departure platform', 'arrival track', 'route', 'arrival station', 'type', 'departure location', 'departure track', 'arrival location', 'class']

    result = 1
    for i, field in enumerate(solution):

        if field.startswith("departure"):
            result *= tickets[0][i]

    print(result)
