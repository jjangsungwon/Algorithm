import sys

sys.setrecursionlimit(10 ** 8)
N = int(sys.stdin.readline())
data = []
dp = [0 for _ in range(N)]
for i in range(N):
    data.append(int(sys.stdin.readline()))
real_sum = -1


def dfs(idx, total, temp):
    global real_sum

    if idx == N-1:
        total += data[idx]
        if total > real_sum:
            real_sum = total
        return

    if (N-1) - idx == 1:
        if temp == 2:
            dfs(idx + 1, total, 0)
        elif temp == 1:
            dfs(idx + 1, total, 0)
        else:
            dfs(idx + 1, total + data[idx], temp + 1)
    else:
        if temp == 2:
            dfs(idx + 1, total, 0)
        elif temp == 1:
            dfs(idx + 1, total + data[idx], temp + 1)
            dfs(idx + 1, total, 0)
        else:
            dfs(idx + 1, total + data[idx], temp + 1)


dfs(0, 0, 0)
print(real_sum)
