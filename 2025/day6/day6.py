def parse_silver(s: str) -> list:
    file = open(s, "r")
    content = file.read().splitlines()
    n = len(content[0].split())
    groupings = [[] for _ in range(n)]

    for line in content:
        operands = line.split()
        for i in range(len(operands)):
            operand = operands[i]
            groupings[i].append(operand)

    return groupings


def solve_silver(s: str):
    groupings = parse_silver(s)

    total = 0
    for group in groupings:
        ans = 0
        if group[-1] == "*":
            ans = 1
            for op in group[: len(group) - 1]:
                ans *= int(op)
        else:
            for op in group[: len(group) - 1]:
                ans += int(op)
        total += ans

    print(f"[SILVER] total is {total} ")


def parse_gold(s: str) -> list:
    file = open(s, "r")
    content = [list(line) for line in file.read().splitlines()]
    groupings = []
    n = len(content)
    m = len(content[0])

    for j in range(m):
        if j < len(content[n - 1]) and (
            content[n - 1][j] == "*" or content[n - 1][j] == "+"
        ):
            groupings.append([content[n - 1][j]])

        op = ""
        for i in range(n - 1):
            if content[i][j].isdigit():
                op += content[i][j]
        if op:
            groupings[-1].append(int(op))

    return groupings


def solve_gold(s: str):
    groupings = parse_gold(s)

    total = 0
    for group in groupings:
        ans = 0
        if group[0] == "*":
            ans = 1
            for op in group[1:]:
                ans *= op
        else:
            for op in group[1:]:
                ans += op

        total += ans

    print(f"[GOLD] total is {total}")


solve_silver("input.txt")
solve_gold("input.txt")
