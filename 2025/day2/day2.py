def get_ranges(sequence: str) -> list:
    file = open(sequence, "r")
    content = file.read().split(",")
    ranges = []
    for line in content:
        bounds = line.split("-")
        ranges.append((int(bounds[0]), int(bounds[1])))

    file.close()
    return ranges


def solve_part1(input: str):
    ranges = get_ranges(input)
    sum = 0
    for r in ranges:
        (lower, upper) = r

        for value in range(lower, upper + 1):
            s = str(value)
            if (len(s) % 2) != 0:
                continue

            mid = len(s) // 2
            if s[0:mid] == s[mid:]:
                sum += value

    print(f"THE PART 1 TOTAL IS: {sum}")


def is_invalid(value: int) -> bool:
    s = str(value)

    for dist in range(1, (len(s) // 2) + 1):
        if len(s) % dist != 0:
            continue
        segments = set()
        for start in range(0, len(s), dist):
            segments.add(s[start : start + dist])
            if len(segments) > 1:
                break

        if len(segments) == 1:
            return True

    return False


def solve_part2(input: str):
    ranges = get_ranges(input)
    sum = 0
    for r in ranges:
        (lower, upper) = r

        for value in range(lower, upper + 1):
            if is_invalid(value):
                sum += value
    print(f"THE PART 1 TOTAL IS: {sum}")


solve_part1("input.txt")
solve_part2("input.txt")
