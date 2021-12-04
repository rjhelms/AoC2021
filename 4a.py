from os import path

INPUT = path.join("input", "4.txt")

BOARD_SIZE = 5


class Tile:
    def __init__(self, number) -> None:
        self.number = number
        self.marked = False

    def check(self, number) -> bool:
        if number == self.number:
            self.marked = True
            return True
        return False

    def __str__(self) -> str:
        out_str = " "
        if self.marked:
            out_str = "*"
        out_str += str(self.number).rjust(2)
        return out_str


class Board:
    def __init__(self, tiles) -> None:
        self.tiles = tiles

    def score_win(self) -> int:
        unmarked = 0
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if not self.tiles[i][j].marked:
                    unmarked += self.tiles[i][j].number
        return unmarked

    def check_win(self) -> int:
        win = False
        # check rows
        for i in range(BOARD_SIZE):
            win = True
            for j in range(BOARD_SIZE):
                win = win and self.tiles[i][j].marked
            if win:
                print("Win in row " + str(i))
                return self.score_win()

        # check columns
        for i in range(BOARD_SIZE):
            win = True
            for j in range(BOARD_SIZE):
                win = win and self.tiles[j][i].marked
            if win:
                print("Win in column " + str(i))
                return self.score_win()

        return 0

    def call_number(self, number) -> int:
        marked = False
        for row in self.tiles:
            for tile in row:
                marked = tile.check(number)
                if marked:
                    return number * self.check_win()
        return 0

    def display(self) -> None:
        out_str = ""
        for row in self.tiles:
            for tile in row:
                out_str += str(tile)
            out_str += "\n"
        print(out_str)


def main() -> None:
    in_lines = []
    boards = []
    with open(INPUT, "r") as in_file:
        in_lines = in_file.read().splitlines()

    called = [int(x) for x in in_lines[0].split(",")]
    print(called)

    tiles = []
    for line in in_lines[2:]:
        if line == "":
            boards.append(Board(tiles))
            tiles = []
        else:
            row = []
            for i in range(0, len(line), 3):
                row.append(Tile(int(line[i : i + 2])))
            tiles.append(row)
    boards.append(Board(tiles))  # do the last one

    for number in called:
        print("Calling " + str(number))

        for board in boards:
            result = board.call_number(number)
            if result > 0:
                print(result)
                return


if __name__ == "__main__":
    main()
