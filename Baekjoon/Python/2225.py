import sys

N, K = map(int, sys.stdin.readline().split())
d = [[0] * 201 for _ in range(201)]


def dp(n, k):
    if k == 1:
        return 1
    elif k == 2:
        return n + 1
    else:
        if d[n][k] != 0:
            return d[n][k]
        else:
            for i in range(n):
                d[n][k] += dp(n - i, k - 1)
            d[n][k] = (d[n][k] + 1) % 1000000000
            return d[n][k]


print(dp(N, K))
