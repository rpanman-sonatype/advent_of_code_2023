import re
from dataclasses import dataclass, field
from typing import List, Tuple

from advent_of_code_2023.help import file_to_lines

EXAMPLE_FILE = "puzzle_example.txt"
PUZZLE_FILE = "puzzle_input.txt"


@dataclass
class Schematic:
    schematic: List[str]
    symbols: List[Tuple[str, int, int]] = field(default_factory=lambda: list())
    numbers: List[Tuple[int, int, int]] = field(default_factory=lambda: list())

    def find_symnbols(self) -> List[Tuple[str, int, int]]:
        self.symbols = list()
        for row, row_contents in enumerate(self.schematic):
            for col, col_contents in enumerate(row_contents):
                if col_contents != "." and not col_contents.isdigit():
                    self.symbols.append((col_contents, int(row), int(col)))
        return self.symbols

    def find_numbers(self) -> List[Tuple[int, int, int]]:
        self.numbers = list()
        for row, row_contents in enumerate(self.schematic):
            for match in re.finditer(r"\d+", row_contents):
                self.numbers.append((int(match.group()), row, match.start()))
        return self.numbers

    def find_numbers_touching_symbol(self, symbol: str = "") -> List[int]:
        self.touching_numbers = list()
        for number, num_row, num_col in self.numbers:
            for _symbol, sym_row, sym_col in self.symbols:
                if abs(num_row - sym_row) <= 1:
                    if sym_col >= num_col - 1 and sym_col <= num_col + len(str(number)):
                        self.touching_numbers.append(number)
                        break
        return self.touching_numbers

    def find_gears(self) -> List[Tuple[str, int, int]]:
        return [point for point in self.symbols if point[0] == "*"]

    def get_score_part_1(self) -> int:
        return sum(self.find_numbers_touching_symbol())

    def get_score_part_2(self) -> int:
        score = 0
        for _symbol, sym_row, sym_col in self.find_gears():
            touching_numbers: List[int] = list()
            for number, num_row, num_col in self.numbers:
                if abs(num_row - sym_row) <= 1:
                    if sym_col >= num_col - 1 and sym_col <= num_col + len(str(number)):
                        touching_numbers.append(number)
            if len(touching_numbers) == 2:
                score += touching_numbers[0] * touching_numbers[1]
        return score


schematic = Schematic(file_to_lines(__file__, PUZZLE_FILE))
schematic.find_symnbols()
schematic.find_numbers()
schematic.find_numbers_touching_symbol()
print(f"Part 1: {schematic.get_score_part_1()}")
print(f"Part 2: {schematic.get_score_part_2()}")
