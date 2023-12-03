import pathlib

from advent_of_code_2023.help import file_to_lines


def get_first_and_last_digit(string: str) -> int:
    return int(
        "".join(map([c for c in string if not c.isalpha()].__getitem__, [0, -1]))
    )


def replace_text_numbers_with_numbers(line: str) -> str:
    number_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    while any(word in line for word in number_map):
        earliest_index = None
        earliest_string = ""

        for string in number_map:
            try:
                (earliest_index, earliest_string) = (
                    (line.index(string), string)
                    if not earliest_index or line.find(string) < earliest_index
                    else (earliest_index, earliest_string)
                )
            except ValueError:
                pass
        line = line.replace(earliest_string, number_map[earliest_string], 1)
    return line


print(
    f"Part 1: {
    sum(
        map(
            get_first_and_last_digit,
                file_to_lines(
                    __file__, "puzzle_input.txt"
                ),
        )
    )}"
)


print(
    f"Part 2: {
    sum(
        map(
            get_first_and_last_digit,
            map(
                replace_text_numbers_with_numbers,
                file_to_lines(
                    __file__, "puzzle_input.txt"
                ),
            ),
        )
    )}"
)

# first answer: 54940
# second answer: 54208
