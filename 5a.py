from os import path

INPUT = path.join("input", "5.txt")


def traverse(line, map):
    current = line[0].copy()
    vector = [0, 0]

    if line[0][0] > line[1][0]:
        vector[0] = -1
    elif line[0][0] < line[1][0]:
        vector[0] = 1

    if line[0][1] > line[1][1]:
        vector[1] = -1
    elif line[0][1] < line[1][1]:
        vector[1] = 1

    while (current[0] != line[1][0]) or (current[1] != line[1][1]):
        map[current[0]][current[1]] += 1
        current[0] += vector[0]
        current[1] += vector[1]

    map[current[0]][current[1]] += 1  # get the last one


def main():
    max_x = 0
    max_y = 0
    lines = []
    with open(INPUT, "r") as in_file:
        for row in in_file:
            coords = row.split(" -> ")
            line = []
            for coord in coords:
                line += [[int(x) for x in coord.split(",")]]
                if int(coord.split(",")[0]) > max_x:
                    max_x = int(coord.split(",")[0])
                if int(coord.split(",")[1]) > max_y:
                    max_y = int(coord.split(",")[1])
            lines.append(line)

    map = [[0 for _ in range(max_y + 1)] for _ in range(max_x + 1)]

    for line in lines:
        if line[0][0] == line[1][0]:
            traverse(line, map)
        elif line[0][1] == line[1][1]:
            traverse(line, map)
        else:
            pass  # ignore diagonals

    score = 0
    for row in map:
        for item in row:
            if item >= 2:
                score += 1

    print(score)


if __name__ == "__main__":
    main()
