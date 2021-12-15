from os import path

INPUT = path.join("input", "12.txt")


def main() -> None:
    with open(INPUT, "r") as in_file:
        paths = {}
        lines = in_file.read().splitlines()
        for line in lines:
            line = line.split("-")
            if line[0] not in paths:
                paths[line[0]] = [line[1]]
            else:
                paths[line[0]].append(line[1])
            if line[1] not in paths:
                paths[line[1]] = [line[0]]
            else:
                paths[line[1]].append(line[0])

    open_list = [["start"]]
    complete_paths = []
    failed_paths = []

    while len(open_list) > 0:
        new_open_list = []
        for path in open_list:
            potential_next = [
                x for x in paths[path[-1]] if x.upper() == x or x not in path
            ]
            if len(potential_next) == 0:
                failed_paths.append(path)
            for step in potential_next:
                new_path = path.copy()
                new_path.append(step)
                if new_path[-1] == "end":
                    complete_paths.append(new_path)
                else:
                    new_open_list.append(new_path)
        open_list = new_open_list

    print(len(complete_paths))


if __name__ == "__main__":
    main()
