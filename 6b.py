from os import path

INPUT = path.join("input", "6.txt")

TICKS = 256


def main():
    growth = [0 for _ in range(TICKS)]
    population = 0

    with open(INPUT, "r") as in_file:
        for line in in_file:
            line = [int(x) for x in line.split(",")]
            for fish in line:
                growth[fish] += 1
            population = len(line)

    for i in range(len(growth)):
        try:
            growth[i + 7] += growth[i]
            growth[i + 9] += growth[i]
        except IndexError:
            pass
        except:
            raise

        population += growth[i]
        print("Day %i: %i" % (i, population))


if __name__ == "__main__":
    main()
