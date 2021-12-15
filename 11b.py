from os import path

INPUT = path.join("input", "11.txt")


def iterate(grid) -> int:
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] += 1

    iteration_flashes = 0
    while True:

        round_flashes = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] > 9:
                    round_flashes += 1
                    grid[y][x] = 0
                    for chk_y in range(y - 1, y + 2):
                        for chk_x in range(x - 1, x + 2):
                            # check that current position is w/in bounds
                            if (
                                chk_y >= 0
                                and chk_x >= 0
                                and chk_y < len(grid)
                                and chk_x < len(grid[0])
                                and (y != chk_y or x != chk_x)
                            ):
                                # if is greater than 0, has no flashed alredy, so increment
                                if grid[chk_y][chk_x] > 0:
                                    grid[chk_y][chk_x] += 1
        if round_flashes == 0:
            return iteration_flashes
        else:
            iteration_flashes += round_flashes


def main() -> None:
    grid = []
    with open(INPUT, "r") as in_file:
        for line in in_file:
            grid_line = [int(x) for x in line.strip()]
            grid.append(grid_line)

    grid_size = len(grid) * len(grid[0])

    iteration = 0
    flashes = 0
    while flashes != grid_size:
        iteration += 1
        flashes = iterate(grid)

    print(iteration)


if __name__ == "__main__":
    main()
