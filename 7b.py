from os import path
import statistics
import math

INPUT = path.join("input", "7.txt")


def calc_fuel(crabs, level):
    fuel = 0
    for crab in crabs:
        dist = abs(crab - level)
        fuel += (dist * (dist + 1)) / 2
    return fuel


def main():
    crabs = []
    with open(INPUT, "r") as in_file:
        for line in in_file:
            crabs = [int(x) for x in line.split(",")]

    mean = statistics.mean(crabs)

    mean_floor = math.floor(mean)
    mean_ceil = math.ceil(mean)

    fuel_floor = calc_fuel(crabs, mean_floor)
    fuel_ceil = calc_fuel(crabs, mean_ceil)

    print("Fuel: %i" % min([fuel_ceil, fuel_floor]))


if __name__ == "__main__":
    main()
