"""
Day Eighteen - Recursion and semantic trees
"""

import re
from typing import Any

import utils


class BinNode:

    def __init__(self, left, right, operation):
        self.left = left
        self.right = right
        self.operation = operation
        self.parent = None


def extract_sub_term_from_right(text: str) -> tuple:
    text = text.strip()

    start_position = None
    end_position = None

    if re.search(r"\)$", text):
        stack = 0
        for i in range(len(text) - 1, -1, -1):
            if text[i] == ")":
                stack += 1
            elif text[i] == "(":
                stack -= 1

            if end_position is None and stack > 0:
                end_position = i

            if stack == 0 and end_position is not None:
                start_position = i
                break

        return (start_position, end_position,
                text[start_position + 1:end_position])
    elif re.search(r"\d+$", text) is not None:
        matched_text = re.search(r"\d*$", text).group()
        return len(text) - len(matched_text), len(text) - 1, matched_text
    else:
        raise ValueError


def extract_sub_term_from_left(text: str) -> tuple:
    text = text.strip()

    start_position = None
    end_position = None

    if re.search(r"^\(", text):
        stack = 0
        for i in range(len(text)):
            if text[i] == "(":
                stack += 1
            elif text[i] == ")":
                stack -= 1

            if start_position is None and stack > 0:
                start_position = i

            if stack == 0 and start_position is not None:
                end_position = i
                break

        return (start_position, end_position,
                text[start_position + 1:end_position])
    elif re.search(r"^\d+", text) is not None:
        matched_text = re.search(r"^\d*", text).group()
        return 0, len(matched_text) - 1, matched_text
    else:
        raise ValueError


def build_tree(text: str, accumulator: Any):
    text = text.strip()

    if text == "":
        return accumulator

    if re.search(r"^\d+$", text) is not None:
        return int(text)

    elif re.search(r"\d+$", text) is not None:
        matched_text = re.search(r"\d*$", text).group()
        number = int(matched_text)
        return build_tree(text[:-len(matched_text)], number)

    elif re.search(r"\+$", text) is not None:
        return BinNode(left=build_tree(text[:-1], None),
                       right=accumulator,
                       operation="+")

    elif re.search(r"\*$", text) is not None:
        return BinNode(left=build_tree(text[:-1], None),
                       right=accumulator,
                       operation="*")

    elif re.search(r"\)$", text) is not None:
        start, end, inside = extract_sub_term_from_right(text)
        tree = build_tree(inside, accumulator)
        return build_tree(text[:start], tree)


def evaluate_tree(tree: Any) -> int:
    if isinstance(tree, BinNode):
        if tree.operation == "+":
            return evaluate_tree(tree.left) + evaluate_tree(tree.right)
        elif tree.operation == "*":
            return evaluate_tree(tree.left) * evaluate_tree(tree.right)
    else:
        return tree


def print_tree(tree: Any) -> int:
    if isinstance(tree, BinNode):
        if isinstance(tree.left, BinNode):
            print("(", end="")
        print_tree(tree.left)
        print(tree.operation, end="")
        print_tree(tree.right)
        if isinstance(tree.left, BinNode):
            print(")", end="")
    else:
        print(tree, end="")


def add_brackets(text: str) -> str:

    i = 0
    while i < len(text):

        if text[i] == "+":
            l_start, l_stop, l_inside = extract_sub_term_from_right(text[:i])
            text = text[:l_start] + "(" + text[l_start:l_stop + 1] + text[l_stop + 1:]
            i += 1

            r_start, r_stop, r_inside = extract_sub_term_from_left(text[i + 2:])
            r_start = i + r_start + 2
            r_stop = i + r_stop + 2
            text = text[:r_start] + text[r_start:r_stop + 1] + ")" + text[r_stop + 1:]

        i += 1

    return text


if __name__ == '__main__':

    lines = utils.read_strings_from_lines("in/day_18.txt")

    result = 0
    for line in lines:
        processed = add_brackets(line)
        t = build_tree(processed, None)
        curr = evaluate_tree(t)
        result += curr

    print(result)


