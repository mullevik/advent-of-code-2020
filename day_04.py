"""
Day Four - Multiple text parsing operations
"""

import utils


def validate_byr(x):
    return 1920 <= int(x) <= 2002


def validate_iyr(x):
    return 2010 <= int(x) <= 2020


def validate_eyr(x):
    return 2020 <= int(x) <= 2030


def validate_hgt(x):
    if x.endswith("cm"):
        x = x.replace("cm", "")
        return 150 <= int(x) <= 193
    elif x.endswith("in"):
        x = x.replace("in", "")
        return 59 <= int(x) <= 76
    return False


def validate_hcl(x):
    if x.startswith("#"):
        x = x.replace("#", "")
        if len(x) == 6:
            valid_chars = "0123456789abcdef"
            for c in x:
                if c not in valid_chars:
                    return False
            return True
    return False


def validate_ecl(x):
    return x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_pid(x):
    if len(x) == 9:
        valid_chars = "0123456789"
        for c in x:
            if c not in valid_chars:
                return False
        return True
    return False


def validate_cid(x):
    return True


if __name__ == '__main__':

    required_keys = [
        ("byr", validate_byr),
        ("iyr", validate_iyr),
        ("eyr", validate_eyr),
        ("hgt", validate_hgt),
        ("hcl", validate_hcl),
        ("ecl", validate_ecl),
        ("pid", validate_pid),
    ]

    optional_keys = [
        ("cid", validate_cid)
    ]

    lines = utils.read_strings_from_lines("in/day_04.txt", strip=False)
    # append blank line after the last passport
    lines.append("\n")

    passports = []

    current_passport = {}

    for line in lines:

        if line == "\n":
            # add current passport to passports and reset it
            passports.append(current_passport)
            print(current_passport)
            current_passport = {}
        else:
            for field in line.strip().split():
                key = field.split(":")[0]
                value = field.split(":")[1]
                current_passport[key] = value

    number_of_valid_passports = 0

    for passport in passports:

        valid = True

        for key,  val_f in required_keys:
            if key not in passport:
                valid = False
            else:
                if not val_f(passport[key]):
                    valid = False

        if valid:
            number_of_valid_passports += 1

    print(number_of_valid_passports)
