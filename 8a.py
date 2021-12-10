from os import path

INPUT = path.join("input", "8.txt")


class DisplayLine:
    def __init__(self, input, output) -> None:
        self.input = input
        self.output = output
        self.mapping = ["" for _ in range(10)]
        self.find_easy()

    def find_easy(self) -> None:
        for digit in self.output:
            if len(digit) == 2:
                self.mapping[1] = digit
            elif len(digit) == 4:
                self.mapping[4] = digit
            elif len(digit) == 3:
                self.mapping[7] = digit
            elif len(digit) == 7:
                self.mapping[8] = digit

    def find_in_output(self, value) -> int:
        count = 0
        for digit in self.output:
            if digit == self.mapping[value]:
                count += 1

        return count


def main() -> None:
    lines = []
    with open(INPUT, "r") as in_file:
        for line in in_file:
            line = line.split("|")
            in_chars = ["".join(sorted(x.strip())) for x in line[0].strip().split(" ")]
            out_chars = ["".join(sorted(x.strip())) for x in line[1].strip().split(" ")]
            lines.append(DisplayLine(in_chars, out_chars))

    count = 0
    for display in lines:
        count += display.find_in_output(1)
        count += display.find_in_output(4)
        count += display.find_in_output(7)
        count += display.find_in_output(8)

    print(count)


if __name__ == "__main__":
    main()
