#github : jjangsungwon.github.io
import sys

sys.setrecursionlimit(10**8)
# input
N = int(sys.stdin.readline())
data = []
d = [0 for _ in range(301)]
for i in range(N):
    data.append(int(sys.stdin.readline()))


def dp(idx):
    if idx == 0:
        return data[0]
    elif idx == 1:
        return data[0] + data[1]
    elif idx == 2:
        return max(data[0] + data[2], data[1] + data[2])

    # memoization
    if d[idx] != 0:
        return d[idx]
    else:
        d[idx] = max(dp(idx - 3) + data[idx - 1] + data[idx], dp(idx - 2) + data[idx])
        return d[idx]


print(dp(N - 1))
