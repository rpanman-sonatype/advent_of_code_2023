import functools
import re

from advent_of_code_2023.help import file_to_lines


def game_id(game_string: str) -> int:
    if id_search := re.search(r"^Game (\d+):", game_string):
        return int(id_search.group(1))
    return 0


def game_record_is_valid(game_record: list[str], max_cubes: dict[str, int]) -> bool:
    if not game_record or not max_cubes:
        return False
    for colour_selection in game_record:
        if matches := re.match(r"(\d+)\s+(.+)", colour_selection):
            if int(matches.group(1)) > max_cubes.get(matches.group(2), -1):
                return False
    return True


def get_game_records(game_string: str) -> list[list[str]]:
    return [
        re.findall(r"(\d+\s[A-z]+)[\s,]*", choice) for choice in game_string.split(";")
    ]


def game_score(game: str, max_cubes: dict[str, int]) -> int:
    for game_record in get_game_records(game):
        if not game_record_is_valid(game_record=game_record, max_cubes=max_cubes):
            return 0
    return game_id(game)


def score_games_part1(games: list[str], max_cubes: dict[str, int]) -> int:
    return functools.reduce(
        lambda a, b: a + game_score(b, max_cubes=max_cubes),
        games,
        0,
    )


def minimum_cubes(game: str) -> dict[str, int]:
    result = {"red": 0, "green": 0, "blue": 0}
    if matches := re.findall(r"(\d+)\s+(blue|green|red)", game):
        for match in matches:
            if int(match[0]) > result[match[1]]:
                result[match[1]] = int(match[0])
    return result


def cube_score(game: str) -> int:
    result = functools.reduce(lambda a, b: a * b, minimum_cubes(game).values(), 1)
    return result


def score_games_part2(games: list[str]) -> int:
    return functools.reduce(lambda a, b: a + cube_score(b), games, 0)


if __name__ == "__main__":
    print(
        f"""Part 1: {
        score_games_part1(
            file_to_lines(
               __file__, "puzzle_input.txt",
            ),
            {"red": 12, "green": 13, "blue": 14},
        )}"""
    )

    print(
        f"""Part 2: {
        score_games_part2(
            file_to_lines(
                __file__, "/puzzle_input.txt",
            ))}"""
    )
