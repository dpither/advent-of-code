from collections import defaultdict
from itertools import combinations


def parse_input(s: str):
    file = open(s, "r")
    content = file.read().splitlines()
    machines = []

    for line in content:
        arr = line.split(" ")
        n = len(arr)
        buttons = []
        for button in arr[1:-1]:
            buttons.append(
                tuple(int(indicator) for indicator in button.strip("()").split(","))
            )
        machines.append(
            [
                arr[0].strip("[]"),
                buttons,
                [int(voltage) for voltage in arr[-1].strip("{}").split(",")],
            ]
        )
    return machines


def press_silver(start, button):
    arr = list(start)
    for i in button:
        if arr[i] == "#":
            arr[i] = "."
        else:
            arr[i] = "#"
    return "".join(arr)


def solve_silver(s: str):
    machines = parse_input(s)
    total_presses = 0

    for goal, buttons, _ in machines:
        presses = 1
        while presses < len(buttons):
            done = False
            for comb in combinations(buttons, presses):
                curr = "." * len(goal)
                for button in comb:
                    curr = press_silver(curr, button)
                if curr == goal:
                    done = True
                    break

            if done:
                total_presses += presses
                break
            presses += 1

    print(f"[SILVER] {total_presses}")


def press_gold(start, button):
    for i in button:
        start[i] += 1


# 1 Equal, -1 Invalid, 0 Less than
def check_gold(curr, goal):
    for i in range(len(curr)):
        if curr[i] > goal[i]:
            return -1
        if curr[i] < goal[i]:
            return 0
    return 1


def solve_gold(s: str):
    machines = parse_input(s)
    total_presses = 0
    max_buttons = max([len(buttons) for _, buttons, goal in machines])

    # for _, buttons, goal in machines:
    #     button_map = defaultdict(list)

    #     def solve_i(curr, goal, i):
    #         combs = button_map[i]

    #     for button in buttons:
    #         for i in button:
    #             button_map[i].append(button)
    #     curr = [0] * len(goal)
    #     for button in buttons:
    #         press_gold(curr, button)

    #     print(curr)
    #     return

    print(max_buttons)
    print(f"[GOLD] ")


# solve_silver("input.txt")
solve_gold("example.txt")
