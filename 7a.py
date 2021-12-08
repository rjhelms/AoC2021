from os import path

INPUT = path.join("input", "7.txt")


def main():
    crabs = []
    with open(INPUT, "r") as in_file:
        for line in in_file:
            crabs = [int(x) for x in line.split(",")]

    crabs.sort()

    median = crabs[round(len(crabs) / 2)]
    print("Median: %i" % median)

    fuel = 0
    for crab in crabs:
        fuel += abs(crab - median)

    print("Fuel: %i" % fuel)


if __name__ == "__main__":
    main()
