import copy, sys


def dfs(graph, start, parent):
    stack = [start]  # 1

    while stack:
        node = stack.pop()
        for i in graph[node]:
            parent[i].append(node)
            stack.append(i)
            graph[i].remove(node)


if __name__ == "__main__":

    N = int(input())
    node = [[] for _ in range(N + 1)]
    parent = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        e1, e2 = map(int, sys.stdin.readline().split())
        node[e1].append(e2)
        node[e2].append(e1)

    dfs(node, 1, parent)
    for i in range(2, N + 1):
        print(parent[i][0])