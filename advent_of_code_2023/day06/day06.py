from functools import reduce
from math import ceil, floor, sqrt

t = 7
d = 9


def solve_quadratic(a: int, b: int, c: int) -> list[float]:
    d = (b**2) - (4 * a * c)

    sol1 = (-b - sqrt(d)) / (2 * a)
    sol2 = (-b + sqrt(d)) / (2 * a)
    return sorted((sol1, sol2))


def get_count_of_possible_times(time: int, distance: int) -> int:
    [sol1, sol2] = solve_quadratic(1, -time, distance)
    if (sol1).is_integer():
        sol1 += 1
    if (sol2).is_integer():
        sol2 -= 1
    sol1 = ceil(sol1)
    sol2 = floor(sol2)
    return int(abs(sol1 - sol2)) + 1


assert get_count_of_possible_times(time=7, distance=9) == 4
assert get_count_of_possible_times(time=15, distance=40) == 8
assert get_count_of_possible_times(time=30, distance=200) == 9

my_inputs = [
    (34, 204),
    (90, 1713),
    (89, 1210),
    (86, 1780),
    # Time:        34     90     89     86
    # Distance:   204   1713   1210   1780
]

part1_answer = reduce(
    lambda x, y: x * y,
    [get_count_of_possible_times(*answer) for answer in my_inputs],
)
part2_answer = get_count_of_possible_times(time=34908986, distance=204171312101780)

assert part1_answer == 633080
assert part2_answer == 20048741

print(f"Part 1: {part1_answer}")
print(f"Part 2: {part2_answer}")
