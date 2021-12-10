from os import path

INPUT = path.join("input", "8.txt")

DIGITS = [
    [0, 1, 2, 4, 5, 6],
    [2, 5],
    [0, 2, 3, 4, 6],
    [0, 2, 3, 5, 6],
    [1, 2, 3, 5],
    [0, 1, 3, 5, 6],
    [0, 1, 3, 4, 5, 6],
    [1, 2, 5],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 5, 6],
]


class DisplayLine:
    def __init__(self, input, output) -> None:
        self.input = input
        self.output = output
        all_digits = self.input.copy()
        for digit in self.output:
            all_digits.append(digit)

        self.unique_digits = []

        for digit in all_digits:
            if digit not in self.unique_digits:
                self.unique_digits.append(digit)

        self.mapping = ["" for _ in range(10)]
        self.segments = ["" for _ in range(7)]

        self.assign_segments()

    def find_easy(self) -> None:
        for digit in self.unique_digits:
            if len(digit) == 2:
                self.mapping[1] = digit
            elif len(digit) == 4:
                self.mapping[4] = digit
            elif len(digit) == 3:
                self.mapping[7] = digit
            elif len(digit) == 7:
                self.mapping[8] = digit

    def assign_segments(self) -> None:
        # every line seems to contain all 10 digits

        #  0000
        # 1    2
        # 1    2
        #  3333
        # 4    5
        # 4    5
        #  6666

        # find the easy digits first
        self.find_easy()

        # segment 0 - in 0, 2, 3, 5, 6, 7, 8, 9
        # in 7 but not in 1
        # this works for every line in input

        for char in self.mapping[7]:
            if char not in self.mapping[1]:
                self.segments[0] = char

        # segments that can be determined by counting occurances

        # segment 1 - 6 times - in 0, 4, 5, 6, 8, 9
        # segment 2 - 8 times, but not segment 0 - in 0, 1, 2, 3, 4, 7, 8, 9
        # segment 4 - 4 times - in 0, 2, 6, 8, 7
        # segment 5 - 9 times - in 0, 1, 3, 4, 5, 6, 7, 8, 9

        for char in "abcdefg":
            count = 0
            for digit in self.unique_digits:
                if char in digit:
                    count += 1

            # ignore ones that are already assigned
            if char not in self.segments:
                if count == 6:
                    self.segments[1] = char
                elif count == 8:
                    self.segments[2] = char
                elif count == 4:
                    self.segments[4] = char
                elif count == 9:
                    self.segments[5] = char

        # digit 2 is the only one that doesn't contain segment 5

        for digit in self.unique_digits:
            if self.segments[5] not in digit:
                self.mapping[2] = digit

        # count unmapped - segment 3 appears in 4 unmapped digits, segment 6 appears in 5 unmapped digits

        # segment 3 - in 2, 3, 4, 5, 6, 8, 9
        # segment 6 - in 0, 2, 3, 5, 6, 8, 9

        for char in "abcdefg":
            if char not in self.segments:
                count = 0
                for digit in self.unique_digits:
                    if char in digit and digit not in self.mapping:
                        count += 1
                if count == 4:
                    self.segments[3] = char
                elif count == 5:
                    self.segments[6] = char

        # determine remaining digit mappings

        for mapping_idx in [0, 3, 5, 6, 9]:
            for segment_idx in DIGITS[mapping_idx]:
                self.mapping[mapping_idx] = (
                    self.mapping[mapping_idx] + self.segments[segment_idx]
                )
            self.mapping[mapping_idx] = "".join(sorted(self.mapping[mapping_idx]))

    def evaluate_output(self) -> int:
        value = 0
        for digit in self.output:
            value *= 10
            value += self.mapping.index(digit)
        return value


def main() -> None:
    lines = []
    with open(INPUT, "r") as in_file:
        for line in in_file:
            line = line.split("|")
            in_chars = ["".join(sorted(x.strip())) for x in line[0].strip().split(" ")]
            out_chars = ["".join(sorted(x.strip())) for x in line[1].strip().split(" ")]
            lines.append(DisplayLine(in_chars, out_chars))

    sum = 0
    for display in lines:
        sum += display.evaluate_output()

    print(sum)


if __name__ == "__main__":
    main()
