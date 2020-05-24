import sys
sys.setrecursionlimit(10**6)


def dfs(v):
    visited[v] = True
    for i in adj[v]:
        if not visited[i]:
            dfs(i)


if __name__ == "__main__":

    N, M = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)

    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    cnt = 0
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(cnt)