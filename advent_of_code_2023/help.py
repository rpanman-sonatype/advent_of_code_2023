import pathlib


def file_to_lines(module_path: str, filename: str) -> list[str]:
    with open(
        str(pathlib.Path(module_path).parent.resolve()) + "/" + filename,
        "r",
        encoding="utf-8",
    ) as the_file:
        return [a.strip() for a in the_file.readlines()]
