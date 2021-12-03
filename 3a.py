from os import path

INPUT = path.join("input", "3.txt")


def main():
    gamma = 0
    epsilon = 0
    lines = 0
    bit_counts = []

    with open(INPUT, "r") as in_file:
        for line in in_file:
            lines += 1
            line = line.strip()
            while len(bit_counts) < len(line):
                bit_counts.append(0)
            for i in range(len(line)):
                if line[i] == "1":
                    bit_counts[i] += 1

    for bit in bit_counts:
        gamma <<= 1
        epsilon <<= 1
        if bit > lines / 2:
            gamma += 1
        else:
            epsilon += 1

    print(gamma * epsilon)


if __name__ == "__main__":
    main()
