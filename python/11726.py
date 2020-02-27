import sys

sys.setrecursionlimit(10 ** 8)


def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        if d[n] != 0:
            return d[n]
        else:
            d[n] = (dp(n - 1) + dp(n - 2)) % 10007
            return d[n]


N = int(sys.stdin.readline())
d = [0 for _ in range(1001)]

print(dp(N))
