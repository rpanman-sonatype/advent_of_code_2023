from advent_of_code_2023.help import file_to_lines

PUZZLE_EXAMPLE = file_to_lines(__file__, "puzzle_example.txt")
PUZZLE_INPUT = file_to_lines(__file__, "puzzle_input.txt")


def get_diffs(puzzle: list[int]) -> int:
    diffs = [j - i for i, j in zip(puzzle[:-1], puzzle[1:])]
    if len(set(diffs)) == 1:
        return puzzle[-1] + diffs[0]
    return puzzle[-1] + get_diffs(diffs)


assert get_diffs(puzzle=[int(a) for a in PUZZLE_EXAMPLE[0].split(" ")]) == 18
assert get_diffs(puzzle=[int(a) for a in PUZZLE_EXAMPLE[1].split(" ")]) == 28
assert get_diffs(puzzle=[int(a) for a in PUZZLE_EXAMPLE[2].split(" ")]) == 68


def get_score(puzzle: list[str]) -> int:
    return sum([get_diffs([int(a) for a in line.split(" ")]) for line in puzzle])


assert get_score(PUZZLE_EXAMPLE) == 114
assert get_score(PUZZLE_INPUT) == 1921197370
