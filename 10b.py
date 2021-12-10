from os import path
import statistics

INPUT = path.join("input", "10.txt")

OPEN_CHARS = ["(", "[", "{", "<"]
CLOSE_CHARS = [")", "]", "}", ">"]

COMPLETION_SCORES = [1, 2, 3, 4]


def main() -> None:
    with open(INPUT, "r") as f:
        lines = f.read().splitlines()

    scores = []

    for line in lines:
        stack = []
        corrupt = False
        for char in line:
            if char in OPEN_CHARS:
                stack.append(OPEN_CHARS.index(char))
            if char in CLOSE_CHARS:
                idx = CLOSE_CHARS.index(char)
                if stack.pop() != idx:
                    corrupt = True
                    break

        if corrupt:
            continue

        score = 0
        for _ in range(len(stack)):
            score *= 5
            score += COMPLETION_SCORES[stack.pop()]

        scores.append(score)

    print(statistics.median(scores))


if __name__ == "__main__":
    main()
