import re
from typing import List, Set

from advent_of_code_2023.help import file_to_lines

PUZZLE_EXAMPLE = file_to_lines(__file__, "puzzle_example.txt")
PUZZLE_INPUT = file_to_lines(__file__, "puzzle_input.txt")


def get_line_score(line: str) -> int:
    numbers_in_both_lists = matching_numbers(line)
    if len(numbers_in_both_lists) == 0:
        return 0
    return int(2 ** (len(numbers_in_both_lists) - 1))


def matching_numbers(line: str) -> Set[int]:
    winning_number_string, guess_number_string = line.split(":")[1].split("|")
    winning_numbers = numbers_in_string(winning_number_string)
    guess_numbers = numbers_in_string(guess_number_string)
    numbers_in_both_lists = winning_numbers & guess_numbers
    return numbers_in_both_lists


def get_matching_number_count(line: str) -> int:
    return len(matching_numbers(line))


def numbers_in_string(string: str) -> Set[int]:
    return {int(number) for number in re.findall(r"\d+", string)}


def get_score_part1(lines: List[str]) -> int:
    return sum([get_line_score(number) for number in lines])


def get_score_part2(lines: List[str]) -> int:
    copies = [1] * len(lines)
    for line_count, line_text in enumerate(lines):
        line_score = len(matching_numbers(line_text))
        copies[line_count + 1 : line_count + line_score + 1] = [
            x + copies[line_count]
            for x in copies[line_count + 1 : line_count + line_score + 1]
        ]
    return sum(copies)


print(f"Part 1: {get_score_part1(PUZZLE_INPUT)}")
print(f"Part 2: {get_score_part2(PUZZLE_INPUT)}")
