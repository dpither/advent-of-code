def parse_input(s: str):
    file = open(s, "r")
    content = file.read()


def solve_silver(s: str):
    _ = parse_input(s)

    print(f"[SILVER] ")


def solve_gold(s: str):
    _ = parse_input(s)

    print(f"[GOLD] ")


solve_silver("example.txt")
solve_gold("example.txt")
