"""
Day Fourteen - bit operations
"""
import copy
import itertools
from typing import List

import utils


def apply_value_mask(decimal: int, mask: str) -> int:
    bit_list = utils.decimal_to_bit_list(decimal, len(mask))

    result = []
    for n_bit, m_bit in zip(bit_list, mask):

        if m_bit == "X":
            result.append(n_bit)
        elif m_bit == "1":
            result.append(True)
        elif m_bit == "0":
            result.append(False)
        else:
            raise NotImplementedError

    return utils.bit_list_to_decimal(result)


def apply_address_mask(address: int, mask: str) -> List[int]:

    bit_address = utils.decimal_to_bit_list(address, len(mask))

    n_floating = mask.count("X")

    masked_address = []
    for n_bit, m_bit in zip(bit_address, mask):

        if m_bit == "X":
            masked_address.append("X")
        elif m_bit == "1":
            masked_address.append(True)
        elif m_bit == "0":
            masked_address.append(n_bit)
        else:
            raise NotImplementedError

    all_masks = []

    for i in range(2 ** n_floating):
        current_address = copy.deepcopy(masked_address)
        assignment = utils.decimal_to_bit_list(i, n_floating)
        assignment_idx = 0

        for j in range(len(current_address)):
            if current_address[j] == "X":
                current_address[j] = assignment[assignment_idx]
                assignment_idx += 1

        assert "X" not in current_address
        all_masks.append(utils.bit_list_to_decimal(current_address))

    return all_masks


if __name__ == '__main__':
    lines = utils.read_strings_from_lines("in/day_14.txt")

    memory = {}

    mask = None

    for line in lines:
        if line.startswith("mask"):
            # parse mask
            mask = line.split()[2]
            bit_len = len(mask)
            assert bit_len == 36
        else:
            # parse memory assignment
            info = line.split()[0]

            address = int(info.split("[")[1].split("]")[0])

            decimal = int(line.split()[2])

            addresses = apply_address_mask(address, mask)

            for address in addresses:
                memory[address] = decimal

    result = 0
    for value in memory.values():
        result += value
    print(result)