"""
Day Eight - Instructions
"""

import utils

if __name__ == '__main__':

    lines = utils.read_strings_from_lines("in/day_08.txt")

    instructions = []
    for line in lines:
        ins = line.split()[0]
        arg = int(line.split()[1])

        instructions.append((ins, arg))

    for i in range(-1, len(instructions)):
        pc = 0
        acc = 0

        pc_history = set()

        while pc not in pc_history and pc < len(instructions):
            pc_history.add(pc)
            ins, arg = instructions[pc]

            if pc == i:  # change jmp to nop and vice versa
                if ins == "jmp":
                    ins = "nop"
                elif ins == "nop":
                    ins = "jmp"

            if ins == "nop":
                pc += 1
            elif ins == "acc":
                acc += arg
                pc += 1
            elif ins == "jmp":
                pc += arg
            else:
                raise NotImplementedError

        if pc < len(instructions):
            print("infinite loop")
        else:
            print(f"program terminated when changing ins. {i}")
            print(f"Acc is: {acc}")
            break



