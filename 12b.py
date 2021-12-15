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

    # remove start and end
    paths.pop("end")
    for key in paths:
        if "start" in paths[key]:
            paths[key].remove("start")

    small_caves = []
    for key in paths:
        if key.upper() != key:
            small_caves.append(key)

    open_list = [["start"]]
    complete_paths = []
    failed_paths = []

    while len(open_list) > 0:
        new_open_list = []
        for path in open_list:
            potential_next = [x for x in paths[path[-1]]]
            failed = False
            two_time_small_caves = 0
            for cave in small_caves:
                if path.count(cave) > 2:
                    failed = True
                elif path.count(cave) == 2:
                    two_time_small_caves += 1
            if two_time_small_caves > 1:
                failed = True
            if len(potential_next) == 0:
                failed = True

            if failed:
                failed_paths.append(path)
            else:
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
