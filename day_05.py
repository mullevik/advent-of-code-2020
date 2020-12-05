"""
Day Five - Binary search
"""

import utils

if __name__ == '__main__':
    lines = utils.read_strings_from_lines("in/day_05.txt")

    N_ROWS = 128
    N_COLS = 8

    seat_ids = []

    for line in lines:

        row_lb = 0
        row_ub = N_ROWS - 1

        col_lb = 0
        col_ub = N_COLS - 1

        for char in line:

            if char == "F":
                row_ub -= (row_ub - row_lb) // 2
                row_ub -= 1
            elif char == "B":
                row_lb += (row_ub - row_lb) // 2
                row_lb += 1
            elif char == "L":
                col_ub -= (col_ub - col_lb) // 2
                col_ub -= 1
            elif char == "R":
                col_lb += (col_ub - col_lb) // 2
                col_lb += 1
            else:
                raise NotImplementedError

        assert row_lb == row_ub
        assert col_lb == col_ub

        seat_ids.append(row_lb * N_COLS + col_lb)

    sorted_ids = list(sorted(seat_ids))
    print(sorted_ids)

    for seat_one, seat_two in utils.pairwise(sorted_ids):

        if seat_one + 2 == seat_two:
            print(f"My seat is {seat_one + 1}")






