def get_banks(source: str) -> list:
    file = open(source, "r")
    banks = file.read().splitlines()
    file.close()
    return banks


def get_joltage(bank: str, num_on: int) -> int:
    batteries = list(bank)
    n = len(batteries)
    out = ""
    start = 0

    while num_on > 0:
        peak = 0
        next_start = start
        for i in range(start, n - (num_on - 1)):
            battery = int(batteries[i])
            if battery > peak:
                peak = battery
                next_start = i + 1
        start = next_start
        out += str(peak)
        num_on -= 1

    return int(out)


def solve_part1(source: str):
    banks = get_banks(source)
    total_joltage = 0
    for bank in banks:
        total_joltage += get_joltage(bank, 2)

    print(f"THE TOTAL OUTPUT JOLTAGE FOR PART 1 IS: {total_joltage}")


def solve_part2(source: str):
    banks = get_banks(source)
    total_joltage = 0
    for bank in banks:
        total_joltage += get_joltage(bank, 12)

    print(f"THE TOTAL OUTPUT JOLTAGE FOR PART 2 IS: {total_joltage}")


solve_part1("input.txt")
solve_part2("input.txt")
