def parse_input(s: str) -> (list, list):
    file = open(s, "r")

    line = file.readline()
    ranges = []
    while line != "\n":
        start, end = line.split("-")
        ranges.append([int(start), int(end)])
        line = file.readline()

    ids = [int(line) for line in file.read().splitlines()]
    return (ranges, ids)


def is_fresh(ranges: list, id: int) -> bool:
    for start, end in ranges:
        if id >= start and id <= end:
            return True

    return False


def solve_silver(s: str):
    num_fresh = 0
    ranges, ids = parse_input(s)
    for id in ids:
        if is_fresh(ranges, id):
            num_fresh += 1

    print(f"[SILVER] THE NUMBER OF FRESH AVAILABLE INGREDIENTS IS: {num_fresh}")


def solve_gold(s: str):
    num_fresh = 0
    ranges, _ = parse_input(s)

    ranges.sort(key=lambda x: x[0])
    collapsed = []
    i = 0
    while i < len(ranges):
        curr = ranges[i]
        while i + 1 < len(ranges) and curr[1] >= ranges[i + 1][0]:
            i += 1
            curr[1] = max(curr[1], ranges[i][1])
        collapsed.append(curr)
        i += 1

    for interval in collapsed:
        num_fresh += interval[1] - interval[0] + 1
    print(f"[GOLD] THE NUMBER OF FRESH AVAILABLE INGREDIENTS IS: {num_fresh}")


solve_silver("input.txt")
solve_gold("input.txt")
