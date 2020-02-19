import sys
import copy

sys.setrecursionlimit(10 ** 8)
# input
N = int(sys.stdin.readline())
# data = [[0] * 10 for _ in range(N)]
data = []
ans = [0 for _ in range(1001)]
flag = 0
visited = []


def dfs(idx, pre):
    global flag
    if idx == N:
        flag = 1
        return

    for i in range(1, data[idx][0] + 1):
        if flag == 1:
            return

        if data[idx][i] != pre and visited[idx][i-1] != 1:
            ans[idx] = data[idx][i]
            visited[idx][i-1] = 1

            dfs(idx + 1, data[idx][i])


if __name__ == "__main__":
    for i in range(N):
        temp = list(map(int, sys.stdin.readline().split()))
        data.append(temp)

    for i in range(N):
        temp = [0 for _ in range(data[i][0])]
        visited.append(temp)

    dfs(0, 0)
    if flag == 0:
        print("-1")
    else:
        for i in range(N):
            print(ans[i])
