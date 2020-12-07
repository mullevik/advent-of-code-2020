"""
Day Seven - BFS / DFS search
"""

import utils

if __name__ == '__main__':

    lines = utils.read_strings_from_lines("in/day_07.txt")

    bags = {}

    for line in lines:

        sp = line.split("contain")

        if "no other" in sp[1]:
            bag_name_info = sp[0].split()
            bag_name = f"{bag_name_info[0]} {bag_name_info[1]}"
            bags[bag_name] = []
        else:
            first_info = sp[0]
            second_info = sp[1]

            bag_name_info = first_info.split()
            bag_name = f"{bag_name_info[0]} {bag_name_info[1]}"

            bags[bag_name] = []

            inside_info = second_info.split(",")

            for inside in inside_info:

                inp = inside.split()

                constraint_name = f"{inp[1]} {inp[2]}"
                constraint_number = int(inp[0])

                bags[bag_name].append((constraint_name, constraint_number))

    queue = ["shiny gold"]
    visited = {"shiny gold"}
    # while queue:
    #     current_bag = queue.pop()
    #
    #     for key, value in bags.items():
    #
    #         for bag in value:
    #
    #             if bag[0] == current_bag:
    #
    #                 if key not in visited:
    #                     queue.append(key)
    #                     visited.add(key)

    # print(visited)
    # print(len(visited) - 1)

    total = 0

    print(bags)
    while queue:
        print(queue)

        current_bag = queue.pop()

        for other in bags[current_bag]:

            bag_name, amount = other

            for i in range(amount):
                total += 1
                queue.append(bag_name)

    print(total)




