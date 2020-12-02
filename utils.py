import warnings


def read_ints_from_lines(file="input.txt"):
    with open(file, "r") as f:
        numbers = []
        for x in f.readlines():
            try:
                numbers.append(int(x))
            except ValueError:
                warnings.warn(f"Can not parse int from '{x}'")
        return numbers


def read_floats_from_lines(file="input.txt"):
    with open(file, "r") as f:
        numbers = []
        for x in f.readlines():
            try:
                numbers.append(float(x))
            except ValueError:
                warnings.warn(f"Can not parse float from '{x}'")
        return numbers


def read_strings_from_lines(file="input.txt", strip=True):
    with open(file, "r") as f:
        lines = [x for x in f.readlines()]
        if strip:
            return [x.strip() for x in lines if x.strip() != ""]
        return [x for x in lines]


def _test_read_ints_from_lines():
    numbers = read_ints_from_lines(file="test_inputs/ints.txt")
    assert len(numbers) == 4
    assert numbers[0] == 12
    assert numbers[1] == 123
    assert numbers[2] == 66
    assert numbers[3] == 50


def _test_read_floats_from_lines():
    numbers = read_floats_from_lines(file="test_inputs/floats.txt")
    assert len(numbers) == 4
    assert numbers[0] == 12.3
    assert numbers[1] == 123.12
    assert numbers[2] == 66.32
    assert numbers[3] == 50.1


def _test_read_strings_from_lines():
    strings = read_strings_from_lines(file="test_inputs/strings.txt")
    assert len(strings) == 3
    assert strings[0] == "hello"
    assert strings[1] == "\"world\""
    assert strings[2] == "what's up"
    strings = read_strings_from_lines(file="test_inputs/strings.txt", strip=False)
    assert len(strings) == 6


if __name__ == '__main__':

    _test_read_ints_from_lines()
    _test_read_floats_from_lines()
    _test_read_strings_from_lines()
