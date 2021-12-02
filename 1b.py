from os import path

INPUT = path.join("input", "1.txt")


def main():
    measurements = []
    window = []
    with open(INPUT, "r") as in_file:
        for line in in_file:
            measurements.append(int(line))

    for i in range(2, len(measurements)):
        window.append(sum(measurements[i - 2 : i + 1]))

    count = 0
    for i in range(1, len(window)):
        if window[i] > window[i - 1]:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
