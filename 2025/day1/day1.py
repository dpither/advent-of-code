DIAL_SIZE = 100


def get_instructions(sequence: str) -> list:
    file = open(sequence, "r")
    content = file.read().splitlines()
    rotations = []
    for line in content:
        direction = line[0]
        distance = int(line[1:])

        rotations.append((direction, distance))
    file.close()
    return rotations


def rotate(start: int, direction: str, distance: int) -> int:
    if direction == "L":
        next = (start - distance) % DIAL_SIZE
    else:
        next = (start + distance) % DIAL_SIZE
    return next


def count_zeros(start: int, direction: str, distance: int) -> int:
    if start == 0:
        return distance // DIAL_SIZE

    if direction == "L" and distance >= start:
        return ((distance - start) // DIAL_SIZE) + 1
    elif direction == "R" and distance >= DIAL_SIZE - start:
        return ((distance - (DIAL_SIZE - start)) // DIAL_SIZE) + 1
    else:
        return 0


def solve_part1(sequence: str):
    instructions = get_instructions(sequence)
    curr = 50
    password = 0

    for instruction in instructions:
        (direction, distance) = instruction
        curr = rotate(curr, direction, distance)
        if curr == 0:
            password += 1

    print(f"THE PART 1 PASSWORD IS: {password}")


def solve_part2(sequence: str):
    instructions = get_instructions(sequence)
    curr = 50
    password = 0

    for instruction in instructions:
        (direction, distance) = instruction
        zeros = count_zeros(curr, direction, distance)
        curr = rotate(curr, direction, distance)
        password += zeros

    print(f"THE PART 2 PASSWORD IS: {password}")


solve_part1("input.txt")
solve_part2("input.txt")
