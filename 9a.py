from os import path

INPUT = path.join("INPUT", "9.txt")


def iterate(grid) -> tuple[int, list]:
    new_grid = []
    for y in range(len(grid)):
        new_grid.append([9 for _ in range(len(grid[0]))])

    changes = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (grid[y][x] < 9) and (
                ((y > 0) and (grid[y - 1][x] < grid[y][x]))
                or (y < (len(grid) - 1) and (grid[y + 1][x] < grid[y][x]))
                or (x > 0 and (grid[y][x - 1] < grid[y][x]))
                or (x < (len(grid[0])) - 1 and (grid[y][x + 1] < grid[y][x]))
            ):
                new_grid[y][x] = 9
                changes += 1
            else:
                new_grid[y][x] = grid[y][x]

    return changes, new_grid


def score(grid) -> int:
    score = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] < 9:
                score += grid[y][x] + 1

    return score


def main() -> None:
    grid = []
    with open(INPUT, "r") as in_file:
        for line in in_file:
            row = []
            for char in line.strip():
                row.append(int(char))
            grid.append(row)

    changes = 1

    while changes > 0:
        changes, grid = iterate(grid)

    print(score(grid))


if __name__ == "__main__":
    main()
