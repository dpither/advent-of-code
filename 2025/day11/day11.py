from collections import defaultdict


def parse_input(s: str):
    file = open(s, "r")
    content = file.read().splitlines()
    graph = defaultdict(list)

    for line in content:
        line = line.split(" ")
        for neighbour in line[1:]:
            graph[line[0][:-1]].append(neighbour)

    return graph


def solve_silver(s: str):
    graph = parse_input(s)
    dp = dict()

    def DFS(node, end):
        if node == end:
            return 1

        if (node, end) in dp:
            return dp[(node, end)]

        paths = 0

        for neighbour in graph[node]:
            paths += DFS(neighbour, end)
        dp[(node, end)] = paths
        return paths

    print(f"[SILVER] {DFS("you","out")}")


def solve_gold(s: str):
    graph = parse_input(s)
    dp = dict()

    def DFS(node, end):
        if node == end:
            return 1

        if (node, end) in dp:
            return dp[(node, end)]

        paths = 0

        for neighbour in graph[node]:
            paths += DFS(neighbour, end)
        dp[(node, end)] = paths
        return paths

    svr_fft = DFS("svr", "fft")
    svr_dac = DFS("svr", "dac")
    dac_fft = DFS("dac", "fft")
    fft_dac = DFS("fft", "dac")
    fft_out = DFS("fft", "out")
    dac_out = DFS("dac", "out")

    print(f"[TEST] {svr_fft*fft_dac*dac_out + svr_dac*dac_fft*fft_out}")


solve_silver("input.txt")
solve_gold("input.txt")
