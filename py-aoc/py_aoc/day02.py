import re
from dataclasses import dataclass

EXAMPLE_RECORD = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


@dataclass
class Bag:
    reds: int
    greens: int
    blues: int


def load_input(day: str) -> list[str]:
    output = []
    with open(f"puzzle_inputs/{day}_input.txt", "r") as file:
        for line in file:
            output.append(line)

    return output


def main():
    configuration = Bag(reds=12, greens=13, blues=14)
    raw_data = load_input("day02")

    print(f"Solution, examples, part 1: { part_one(EXAMPLE_RECORD, configuration)}")
    print(f"Solution, examples, part 2: {part_two(EXAMPLE_RECORD)}")
    print(f"Solution part one: {part_one(raw_data, configuration)}")
    print(f"Solution part two: {part_two(raw_data)}")


def parse_game(e: list) -> list:
    record = e[e.find(":") :]
    draws = record.split(";")
    draws = [sample.split(",") for sample in draws]

    draw = []
    for sample in draws:
        quantities = []
        for color in sample:
            quantities.append(re.findall(r"\w+", color))
        draw.append(quantities)
    return draw


def encode_trial(d):
    trial = Bag(reds=0, greens=0, blues=0)
    for color in d:
        if color[1] == "red":
            trial.reds = int(color[0])
        elif color[1] == "green":
            trial.greens = int(color[0])
        elif color[1] == "blue":
            trial.blues = int(color[0])
    return trial


def check_possible_trial(configuration: Bag, draw: list) -> list:
    trials = []
    for d in draw:
        trial = encode_trial(d)

        if (
            (trial.reds > configuration.reds)
            or (trial.greens > configuration.greens)
            or (trial.blues > configuration.blues)
        ):
            trials.append(trial)
    return trials


def check_fewest_config(draw: list) -> list:
    max_reds = 0
    max_greens = 0
    max_blues = 0

    for d in draw:
        trial = encode_trial(d)

        if trial.reds > max_reds:
            max_reds = trial.reds
        if trial.greens > max_greens:
            max_greens = trial.greens
        if trial.blues > max_blues:
            max_blues = trial.blues

    return (max_reds, max_greens, max_blues)


def part_one(games: list[str], configuration: Bag) -> int:
    id_sum = 0
    for i, e in enumerate(games):
        id = i + 1
        draw = parse_game(e)
        trials = check_possible_trial(configuration, draw)

        if len(trials) == 0:
            id_sum += id

    return id_sum


def part_two(games: list[str]) -> int:
    game_powers = []
    for i, e in enumerate(games):
        draw = parse_game(e)
        max_reds, max_greens, max_blues = check_fewest_config(draw)
        power = max_reds * max_greens * max_blues
        game_powers.append(power)

    return sum(game_powers)


if __name__ == "__main__":
    main()
