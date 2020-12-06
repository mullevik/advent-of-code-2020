"""
Day Six - Sets (intersection)
"""

import utils

if __name__ == '__main__':
    lines = utils.read_strings_from_lines("in/day_06.txt", strip=False)
    lines.append("\n")

    groups = []

    current_people = []
    for line in lines:

        if line == "\n":
            groups.append(set.intersection(*current_people))
            current_people = []
        else:
            answers = line.strip()

            person = set()
            for character in answers:
                person.add(character)

            current_people.append(person)

    total = 0
    for group in groups:
        print(group)
        total += len(group)

    print(total)
