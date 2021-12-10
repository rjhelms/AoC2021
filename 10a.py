from os import path

INPUT = path.join("input", "10.txt")

OPEN_CHARS = ["(", "[", "{", "<"]
CLOSE_CHARS = [")", "]", "}", ">"]

ERROR_SCORES = [3, 57, 1197, 25137]


def main() -> None:
    with open(INPUT, "r") as f:
        lines = f.read().splitlines()

    score = 0

    for line in lines:
        stack = []
        for char in line:
            if char in OPEN_CHARS:
                stack.append(OPEN_CHARS.index(char))
            if char in CLOSE_CHARS:
                idx = CLOSE_CHARS.index(char)
                if stack.pop() != idx:
                    score += ERROR_SCORES[idx]
                    break

    print(score)


if __name__ == "__main__":
    main()
