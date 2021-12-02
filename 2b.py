from os import path

INPUT = path.join("input", "2.txt")


def main():
    x_pos = 0
    y_pos = 0
    aim = 0
    with open(INPUT, "r") as in_file:
        for line in in_file:
            if line.split()[0] == "forward":
                x_pos += int(line.split()[1])
                y_pos += int(line.split()[1]) * aim
            elif line.split()[0] == "up":
                aim -= int(line.split()[1])
            elif line.split()[0] == "down":
                aim += int(line.split()[1])

    print(x_pos * y_pos)


if __name__ == "__main__":
    main()
