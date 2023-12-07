from dataclasses import dataclass

from advent_of_code_2023.help import file_to_lines

PUZZLE_EXAMPLE = file_to_lines(__file__, "puzzle_example.txt")
PUZZLE_INPUT = file_to_lines(__file__, "puzzle_input.txt")


@dataclass
class Hand:
    hand: str
    bid: int
    with_jokers: bool = False

    def __post_init__(self) -> None:
        face_card_replacements = {
            "A": "e",
            "K": "d",
            "Q": "c",
            "J": "b",
            "T": "a",
        }
        if self.with_jokers:
            face_card_replacements["J"] = "1"

        for original, new in face_card_replacements.items():
            self.hand = self.hand.replace(original, new)

    def _get_groups(self) -> dict[str, int]:
        return {
            card: self.hand.count(card)
            for card in self.hand
            if self.hand.count(card) > 1
        }

    @property
    def _hand_value(self) -> int:
        groups = self._get_groups()
        if 5 in groups.values():
            return 6
        if 4 in groups.values():
            return 5
        if 3 in groups.values() and 2 in groups.values():
            return 4
        if 3 in groups.values():
            return 3
        if list(groups.values()) == [2, 2]:
            return 2
        if 2 in groups.values():
            return 1
        return 0

    def __lt__(self, other: "Hand") -> bool:
        if self._hand_value == other._hand_value:
            return self.hand < other.hand
        return self._hand_value < other._hand_value

    def __gt__(self, other: "Hand") -> bool:
        if self._hand_value == other._hand_value:
            return self.hand < other.hand
        return self._hand_value > other._hand_value


def score_hands_part1(PUZZLE_EXAMPLE: list[str]) -> int:
    hands = get_hands(PUZZLE_EXAMPLE)
    score = sum([(index + 1) * hand.bid for (index, hand) in enumerate(sorted(hands))])
    return score


def get_hands(PUZZLE_EXAMPLE: list[str]) -> list[Hand]:
    hands = [
        Hand(line.split(" ")[0], int(line.split(" ")[1])) for line in PUZZLE_EXAMPLE
    ]

    return hands


assert score_hands_part1(PUZZLE_EXAMPLE) == 6440
assert score_hands_part1(PUZZLE_INPUT) == 253954294
