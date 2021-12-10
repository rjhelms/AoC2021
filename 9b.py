from os import path

INPUT = path.join("INPUT", "9.txt")


def find_minima_iterate(grid) -> tuple[int, list]:
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


def find_basin_centers(minima_grid, basin_grid) -> int:
    basin_idx = 0

    for y in range(len(minima_grid)):
        for x in range(len(minima_grid[0])):
            if minima_grid[y][x] < 9:
                basin_idx += 1
                basin_grid[y][x] = basin_idx

    return basin_idx


def find_basin_iterate(basin_grid, orig_grid) -> int:
    changes = 0
    for y in range(len(basin_grid)):
        for x in range(len(basin_grid[0])):
            if basin_grid[y][x] == 0 and orig_grid[y][x] < 9:
                if (y > 0) and (basin_grid[y - 1][x] > 0):
                    basin_grid[y][x] = basin_grid[y - 1][x]
                elif (y < (len(basin_grid) - 1)) and (basin_grid[y + 1][x] > 0):
                    basin_grid[y][x] = basin_grid[y + 1][x]
                elif (x > 0) and (basin_grid[y][x - 1] > 0):
                    basin_grid[y][x] = basin_grid[y][x - 1]
                elif (x < (len(basin_grid[0]) - 1)) and (basin_grid[y][x + 1] > 0):
                    basin_grid[y][x] = basin_grid[y][x + 1]

                if basin_grid[y][x] != 0:
                    changes += 1

    return changes


def score_basins(basin_grid, basin_count) -> int:
    basin_sizes = [0 for _ in range(basin_count)]
    for y in range(len(basin_grid)):
        for x in range(len(basin_grid[0])):
            if basin_grid[y][x] > 0:
                basin_sizes[basin_grid[y][x] - 1] += 1

    basin_sizes.sort()

    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


def main() -> None:
    grid = []
    with open(INPUT, "r") as in_file:
        for line in in_file:
            row = []
            for char in line.strip():
                row.append(int(char))
            grid.append(row)

    changes = 1

    minima_grid = grid.copy()

    while changes > 0:
        changes, minima_grid = find_minima_iterate(minima_grid)

    basin_grid = []
    for row in grid:
        basin_grid.append([0 for _ in range(len(grid[0]))])

    basin_count = find_basin_centers(minima_grid, basin_grid)

    changes = 1
    while changes > 0:
        changes = find_basin_iterate(basin_grid, grid)

    print(score_basins(basin_grid, basin_count))


if __name__ == "__main__":
    main()
