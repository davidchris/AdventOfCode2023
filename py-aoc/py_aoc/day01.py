from pytest import fixture


def main():
    raw_data = load_input()
    parsed_lines = [parse_line(line) for line in raw_data]
    first_last_digits = [first_last_digit(word) for word in parsed_lines]
    combined_digits = [
        combine_digits(fl_digits) for fl_digits in first_last_digits
    ]

    print(sum(combined_digits))


def load_input() -> list[str]:
    output = []
    with open("day01_input.txt", "r") as file:
        for line in file:
            output.append(line)

    return output


def parse_line(line: str) -> list[int]:
    word_digit = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    result = []
    for i, e in enumerate(line):
        remaining_line = line[i:]
        found_digit_words = [
            i for i in list(word_digit.keys()) if remaining_line.startswith(i)
        ]
        if len(found_digit_words) != 0:
            dw = found_digit_words[0]
            d = word_digit[dw]
            result.append(d)
        if e.isdigit():
            result.append(int(e))
    return result


def first_last_digit(digits: list[int]) -> tuple[int]:
    return (digits[0], digits[-1])


def combine_digits(fl_digits: tuple[int]) -> int:
    m = 1
    while m <= fl_digits[1]:
        m *= 10
    combined = fl_digits[0] * m + fl_digits[1]

    return combined


class TestParser:
    @fixture
    def examples(self):
        return [
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet",
            # part two examples
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ]

    def test_parse_input(self, examples):
        assert [1, 2] == parse_line(examples[0])
        assert [3, 8] == parse_line(examples[1])
        assert [1, 2, 3, 4, 5] == parse_line(examples[2])
        assert [7] == parse_line(examples[3])
        # part two
        assert [2, 1, 9] == parse_line(examples[4])
        assert [8, 2, 3] == parse_line(examples[5])
        assert [1, 2, 3] == parse_line(examples[6])
        assert [2, 1, 3, 4] == parse_line(examples[7])
        assert [4, 9, 8, 7, 2] == parse_line(examples[8])
        assert [1, 8, 2, 3, 4] == parse_line(examples[9])
        assert [7, 6] == parse_line(examples[10])

    def test_first_last_digit(self, examples):
        assert (1, 2) == first_last_digit(parse_line(examples[0]))
        assert (3, 8) == first_last_digit(parse_line(examples[1]))
        assert (1, 5) == first_last_digit(parse_line(examples[2]))
        assert (7, 7) == first_last_digit(parse_line(examples[3]))
        # part two
        assert (2, 9) == first_last_digit(parse_line(examples[4]))
        assert (8, 3) == first_last_digit(parse_line(examples[5]))
        assert (1, 3) == first_last_digit(parse_line(examples[6]))
        assert (2, 4) == first_last_digit(parse_line(examples[7]))
        assert (4, 2) == first_last_digit(parse_line(examples[8]))
        assert (1, 4) == first_last_digit(parse_line(examples[9]))
        assert (7, 6) == first_last_digit(parse_line(examples[10]))

    def test_combined(self, examples):
        assert 12 == combine_digits(first_last_digit(parse_line(examples[0])))
        assert 38 == combine_digits(first_last_digit(parse_line(examples[1])))
        assert 15 == combine_digits(first_last_digit(parse_line(examples[2])))
        assert 77 == combine_digits(first_last_digit(parse_line(examples[3])))
        assert 29 == combine_digits(first_last_digit(parse_line(examples[4])))
        assert 83 == combine_digits(first_last_digit(parse_line(examples[5])))
        assert 13 == combine_digits(first_last_digit(parse_line(examples[6])))
        assert 24 == combine_digits(first_last_digit(parse_line(examples[7])))
        assert 42 == combine_digits(first_last_digit(parse_line(examples[8])))
        assert 14 == combine_digits(first_last_digit(parse_line(examples[9])))
        assert 76 == combine_digits(first_last_digit(parse_line(examples[10])))


if __name__ == "__main__":
    main()
