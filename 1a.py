from os import path

INPUT = path.join("input", "1.txt")


def main():
    measurements = []
    with open(INPUT, "r") as in_file:
        for line in in_file:
            measurements.append(int(line))

    count = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
