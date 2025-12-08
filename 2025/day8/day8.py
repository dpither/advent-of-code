from collections import defaultdict


def parse_input(s: str):
    file = open(s, "r")
    coords = [
        tuple(int(axis) for axis in line.split(","))
        for line in file.read().splitlines()
    ]
    return coords


def solve_silver(s: str, connections):
    coords = parse_input(s)
    n = len(coords)

    edges = []
    for i in range(n - 1):
        s_x, s_y, s_z = coords[i]
        for j in range(i + 1, n):
            e_x, e_y, e_z = coords[j]
            distance = pow(s_x - e_x, 2) + pow(s_y - e_y, 2) + pow(s_z - e_z, 2)
            edges.append((distance, i, j))

    edges.sort(key=lambda x: x[0])
    graph = defaultdict(list)

    for i in range(connections):
        _, start, end = edges[i]
        graph[start].append(end)
        graph[end].append(start)

    visited = set()

    def DFS(i):
        visited.add(i)
        count = 1
        for neighbour in graph[i]:
            if neighbour not in visited:
                count += DFS(neighbour)
        return count

    circuits = []
    for key in graph:
        if key not in visited:
            circuits.append(DFS(key))

    circuits.sort(reverse=True)
    ans = 1
    for circuit in circuits[:3]:
        ans *= circuit

    print(f"[SILVER] {ans}")


def solve_gold(s: str):
    coords = parse_input(s)
    n = len(coords)
    edges = []
    for i in range(n - 1):
        s_x, s_y, s_z = coords[i]
        for j in range(i + 1, n):
            e_x, e_y, e_z = coords[j]
            distance = pow(s_x - e_x, 2) + pow(s_y - e_y, 2) + pow(s_z - e_z, 2)
            edges.append((distance, i, j))
    edges.sort(key=lambda x: x[0])

    # Use Kruskals to find the edge added last to the minimum spanning tree
    rank = [1] * n
    parent = list(range(n))

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(start, end):
        s_p = find(start)
        e_p = find(end)
        if s_p != e_p:
            if rank[s_p] < rank[e_p]:
                parent[s_p] = e_p
            elif rank[s_p] > rank[e_p]:
                parent[e_p] = s_p
            else:
                parent[e_p] = s_p
                rank[s_p] += 1

    ans = -1
    count = 0
    for _, start, end in edges:
        if find(start) != find(end):
            union(start, end)
            count += 1
            if count == n - 1:
                ans = coords[start][0] * coords[end][0]
                break

    print(f"[GOLD] {ans}")


solve_silver("input.txt", 1000)
solve_gold("input.txt")
