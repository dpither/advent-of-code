def parse_input(s: str):
    file = open(s, "r")
    content = [
        tuple(int(coord) for coord in line.split(","))
        for line in file.read().splitlines()
    ]
    return content


def solve_silver(s: str):
    red_tiles = parse_input(s)
    n = len(red_tiles)
    largest = 0

    for i in range(n - 1):
        for j in range(i, n):
            area = (abs(red_tiles[i][0] - red_tiles[j][0]) + 1) * (
                abs(red_tiles[i][1] - red_tiles[j][1]) + 1
            )
            largest = max(largest, area)

    print(f"[SILVER] {largest}")


# NOT GENERAL SOLUTION, NEED TO CHECK CORNERS ARE INSIDE TOO
def solve_gold(s: str):
    red_tiles = parse_input(s)
    n = len(red_tiles)
    v_edges = []
    h_edges = []

    # Get edges
    for i in range(n):
        curr = red_tiles[i]
        next = red_tiles[(i + 1) % n]
        # Vertical Edge
        if curr[0] == next[0]:
            v_edges.append(
                ((curr[0], min(curr[1], next[1])), (curr[0], max(curr[1], next[1])))
            )
        # Horizontal Edge
        else:
            h_edges.append(
                ((min(curr[0], next[0]), curr[1]), (max(curr[0], next[0]), curr[1]))
            )

    def valid(vertices) -> bool:
        bl, tl, br, tr = vertices
        # Check if vertical edges in graph cross into horizontal edges in square
        for start, end in v_edges:
            # Check bounds
            if start[0] > tl[0] and start[0] < tr[0]:
                # Check if collision, (start, outside end inside, start inside)
                if (start[1] < bl[1] and end[1] > bl[1]) or (
                    start[1] < tl[1] and start[1] >= bl[1]
                ):
                    return False

        # Check if horizontal edges in graph cross into vertical edges in square
        for start, end in h_edges:
            # Check if in bounds
            if start[1] > bl[1] and start[1] < tl[1]:
                # Check if collision, (start outside end inside, start inside)
                if (start[0] < tl[0] and end[0] > tl[0]) or (
                    start[0] < tr[0] and start[0] >= tl[0]
                ):
                    return False
        return True

    largest = 0

    # Go through all pairs and check if valid
    for i in range(n - 1):
        first = red_tiles[i]
        for j in range(i, n):
            second = red_tiles[j]
            area = 0
            # Vertical line/Horizontal Line
            if first[0] == second[0] or first[1] == second[1]:
                area = (abs(first[0] - second[0]) + 1) * (abs(first[1] - second[1]) + 1)
            else:
                vertices = []
                for col in [min(first[0], second[0]), max(first[0], second[0])]:
                    for row in [min(first[1], second[1]), max(first[1], second[1])]:
                        vertices.append((col, row))
                if valid(vertices):
                    area = (abs(first[0] - second[0]) + 1) * (
                        abs(first[1] - second[1]) + 1
                    )

            largest = max(largest, area)

    print(f"[GOLD] {largest}")


solve_silver("input.txt")
solve_gold("input.txt")
