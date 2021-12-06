from os import path

INPUT = path.join("input", "6.txt")


class Fish:
    def __init__(self, timer) -> None:
        self.timer = timer

    def tick(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            return Fish(8)
        return None

    def __repr__(self) -> str:
        return "Fish (%i)" % self.timer


def main():
    school = []
    tick = 0
    with open(INPUT, "r") as in_file:
        for line in in_file:
            school = [Fish(int(x)) for x in line.split(",")]

    while tick < 80:

        new_school = school.copy()
        for fish in school:
            val = fish.tick()
            if val is not None:
                new_school.append(val)
        school = new_school
        tick += 1
        print("Day %i: %i" % (tick, len(school)))

    pass


if __name__ == "__main__":
    main()
