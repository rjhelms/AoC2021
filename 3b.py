from os import path

INPUT = path.join("input", "3.txt")


def main():
    lines = 0
    bit_counts = []
    candidate_lines = []

    with open(INPUT, "r") as in_file:
        for line in in_file:
            lines += 1
            line = line.strip()
            candidate_lines.append(line)
            while len(bit_counts) < len(line):
                bit_counts.append(0)

    oxygen_candidates = candidate_lines.copy()
    co2_candidates = candidate_lines.copy()

    for i in range(len(bit_counts)):
        bit_counts[i] = 0
        for line in oxygen_candidates:
            if line[i] == "1":
                bit_counts[i] += 1

        new_oxygen = []
        oxygen_target = ""
        if bit_counts[i] >= len(oxygen_candidates) / 2:
            oxygen_target = "1"
        else:
            oxygen_target = "0"
        for line in oxygen_candidates:
            if line[i] == oxygen_target:
                new_oxygen.append(line)

        oxygen_candidates = new_oxygen
        if len(oxygen_candidates) == 1:
            break

    for i in range(len(bit_counts)):
        bit_counts[i] = 0
        for line in co2_candidates:
            if line[i] == "1":
                bit_counts[i] += 1

        new_co2 = []
        co2_target = ""
        if bit_counts[i] >= len(co2_candidates) / 2:
            co2_target = "0"
        else:
            co2_target = "1"
        for line in co2_candidates:
            if line[i] == co2_target:
                new_co2.append(line)

        co2_candidates = new_co2
        if len(co2_candidates) == 1:
            break

    print(int(oxygen_candidates[0], 2) * int(co2_candidates[0], 2))


if __name__ == "__main__":
    main()
