def parse_input(s: str):
    file = open(s, "r")
    diagram = [list(line) for line in file.read().splitlines()]
    return diagram


def solve_silver(s: str):
    diagram = parse_input(s)
    n = len(diagram)
    m = len(diagram[0])
    splits = 0

    for i in range(1, n):
        for j in range(m):
            if diagram[i - 1][j] == "S" or diagram[i - 1][j] == "|":
                if diagram[i][j] == "^":
                    splits += 1
                    if j > 0:
                        diagram[i][j - 1] = "|"
                    if j < m - 2:
                        diagram[i][j + 1] = "|"
                else:
                    diagram[i][j] = "|"

    print(f"[SILVER] {splits}")


def solve_gold(s: str):
    diagram = parse_input(s)
    n = len(diagram)
    m = len(diagram[0])
    dp = [[0] * m for _ in range(n)]

    for j in range(m):
        if diagram[0][j] == "S":
            dp[0][j] = 1

    for i in range(1, n):
        for j in range(m):
            if diagram[i - 1][j] == "S" or diagram[i - 1][j] == "|":
                if diagram[i][j] == "^":
                    if j > 0:
                        diagram[i][j - 1] = "|"
                        dp[i][j - 1] += dp[i - 1][j]
                    if j < m - 1:
                        diagram[i][j + 1] = "|"
                        dp[i][j + 1] += dp[i - 1][j]
                else:
                    diagram[i][j] = "|"
                dp[i][j] += dp[i - 1][j]

    print(f"[GOLD] {sum(dp[-1])}")


solve_silver("input.txt")
solve_gold("input.txt")
