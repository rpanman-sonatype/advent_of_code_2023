from advent_of_code_2023.help import file_to_lines

PUZZLE_EXAMPLE = file_to_lines(__file__, "puzzle_example.txt")
PUZZLE_INPUT = file_to_lines(__file__, "puzzle_input.txt")


def get_diffs_forward(puzzle: list[int]) -> int:
    diffs = [j - i for i, j in zip(puzzle[:-1], puzzle[1:])]
    if len(set(diffs)) == 1:
        return puzzle[-1] + diffs[0]
    return puzzle[-1] + get_diffs_forward(diffs)


def get_diffs_backward(puzzle: list[int]) -> int:
    return get_diffs_forward(list(reversed(puzzle)))


def get_score(puzzle: list[str], reversed: bool = False) -> int:
    if not reversed:
        return sum(
            [get_diffs_forward([int(a) for a in line.split(" ")]) for line in puzzle]
        )
    return sum(
        [get_diffs_backward([int(a) for a in line.split(" ")]) for line in puzzle]
    )


# Example
assert get_diffs_forward(puzzle=[int(a) for a in PUZZLE_EXAMPLE[0].split(" ")]) == 18
assert get_diffs_forward(puzzle=[int(a) for a in PUZZLE_EXAMPLE[1].split(" ")]) == 28
assert get_diffs_forward(puzzle=[int(a) for a in PUZZLE_EXAMPLE[2].split(" ")]) == 68
assert get_score(PUZZLE_EXAMPLE) == 114

# Part 1
assert get_score(PUZZLE_INPUT) == 1921197370

# Part 2
assert get_score(PUZZLE_INPUT, reversed=True) == 1124
