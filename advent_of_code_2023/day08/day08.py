import re
from typing import Tuple

from advent_of_code_2023.help import file_to_lines

PUZZLE_EXAMPLE = file_to_lines(__file__, "puzzle_example.txt")
PUZZLE_INPUT = file_to_lines(__file__, "puzzle_input.txt")
MY_EXAMPLE = file_to_lines(__file__, "my_example.txt")


def direction(puzzle: list[str]) -> str:
    return puzzle[0]


def get_instructions(puzzle: list[str]) -> dict[str, Tuple[str, str]]:
    return {
        x[0]: (x[1], x[2])
        for x in [re.findall(r"[A-Z]{3}", line) for line in puzzle[2:]]
    }


def get_route(
    instructions: dict[str, Tuple[str, str]],
    direction: str,
    route: list[str] = ["AAA"],
    end: str = "ZZZ",
) -> list[str]:
    while True:
        side = 0 if direction[(len(route) - 1) % len(direction)] == "L" else 1
        next_hop = instructions[route[-1]][side]
        route.append(next_hop)
        if next_hop == end:
            return route


def get_score(puzzle: list[str]) -> int:
    return len(get_route(get_instructions(puzzle), direction=direction(puzzle))) - 1


assert get_score(PUZZLE_EXAMPLE) == 2
assert get_score(MY_EXAMPLE) == 2
assert get_score(PUZZLE_INPUT) == 15989
