import sys


if __name__ == '__main__':

    lines = [x for x in sys.stdin.readlines()]

    valid_lines = 0

    for line in lines:
        line_sequence = line.split(":")
        rule = line_sequence[0]
        pw = line_sequence[1]

        n_times = rule.split(" ")[0]
        char = rule.split(" ")[1]

        number_one = int(n_times.split("-")[0])
        number_two = int(n_times.split("-")[1])

        if (pw[number_one] == char or pw[number_two] == char) and \
                not (pw[number_one] == char and pw[number_two] == char):
            print(line[:-1])
            valid_lines += 1

    print(valid_lines)