def get_grid(s: str) -> list:
    file = open(s, "r")
    content = file.read().splitlines()
    grid = []

    for line in content:
        grid.append(list(line))

    return grid


def can_access(grid: list, i: int, j: int) -> bool:
    neighbours = 0
    if is_roll(grid, i - 1, j):
        neighbours += 1
    if is_roll(grid, i + 1, j):
        neighbours += 1
    if is_roll(grid, i, j - 1):
        neighbours += 1
    if is_roll(grid, i, j + 1):
        neighbours += 1
    if is_roll(grid, i + 1, j + 1):
        neighbours += 1
    if is_roll(grid, i - 1, j + 1):
        neighbours += 1
    if is_roll(grid, i + 1, j - 1):
        neighbours += 1
    if is_roll(grid, i - 1, j - 1):
        neighbours += 1
    return neighbours < 4


def is_roll(grid: list, i: int, j: int) -> bool:
    if i < 0:
        return False
    if j < 0:
        return False
    if i >= len(grid):
        return False
    if j >= len(grid[0]):
        return False

    return grid[i][j] == "@"


def solve_part1(s: str):
    grid = get_grid(s)
    accessible = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@" and can_access(grid, i, j):
                accessible += 1

    print(f"THE NUMBER OF ACCESSIBLE ROLLS IN PART 1 IS: {accessible}")


def solve_part2(s: str):
    grid = get_grid(s)
    accessible = 0
    prev = -1
    while accessible != prev:
        prev = accessible
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "@" and can_access(grid, i, j):
                    grid[i][j] = "x"
                    accessible += 1

    print(f"THE NUMBER OF ACCESSIBLE ROLLS IN PART 2 IS: {accessible}")


solve_part1("input.txt")
solve_part2("input.txt")
