import pytest

from advent_of_code_2023.day02.day2 import (
    game_id,
    game_record_is_valid,
    game_score,
    get_game_records,
    minimum_cubes,
    score_games_part1,
)


class TestGameId:
    @pytest.mark.parametrize(
        "input, result", [("Game 1:", 1), ("BGame 2:", 0), ("Argle", 0)]
    )
    def test_inputs(self, input: str, result: int) -> None:
        assert game_id(input) == result

    @pytest.mark.parametrize(
        "game_record, max_cubes, result",
        [
            (["2 blue"], {"blue": 1}, False),
            (["1 blue"], {"blue": 2}, True),
            (["1 blue"], {}, False),
            ([], {"blue": 1}, False),
        ],
    )
    def test_game_is_valid(
        self, game_record: list[str], max_cubes: dict[str, int], result: bool
    ) -> None:
        assert (
            game_record_is_valid(game_record=game_record, max_cubes=max_cubes) == result
        )

    def test_get_game_records(self) -> None:
        assert get_game_records("Game 1: 1 blue, 2 red; 2 green, 7 orange") == [
            ["1 blue", "2 red"],
            ["2 green", "7 orange"],
        ]
        assert get_game_records("Game 1: 1 blue, 2 red; 2 green, 7 orange") == [
            ["1 blue", "2 red"],
            ["2 green", "7 orange"],
        ]

    @pytest.mark.parametrize(
        "game_string, max_cubes, result",
        [
            (
                "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                {"red": 12, "green": 13, "blue": 14},
                1,
            ),
            ("Game 2: 2 blue", {"blue": 1}, 0),
        ],
    )
    def test_game_score(
        self, game_string: str, max_cubes: dict[str, int], result: int
    ) -> None:
        assert (
            game_score(
                game_string,
                max_cubes=max_cubes,
            )
            == result
        )

    @pytest.mark.parametrize(
        "game_strings, max_cubes, result",
        [
            (
                [
                    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                    "Game 2: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                ],
                {"red": 12, "green": 13, "blue": 14},
                3,
            ),
            (
                [
                    "Game 3: 2 blue",
                    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                ],
                {"blue": 1},
                0,
            ),
        ],
    )
    def test_score_games(
        self, game_strings: list[str], max_cubes: dict[str, int], result: int
    ) -> None:
        assert (
            score_games_part1(
                game_strings,
                max_cubes=max_cubes,
            )
            == result
        )

    def test_minumum_cubes(self) -> None:
        assert minimum_cubes(
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        ) == {"blue": 6, "green": 2, "red": 4}
