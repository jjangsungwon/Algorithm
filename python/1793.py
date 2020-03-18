import sys

sys.setrecursionlimit(10 ** 8)

d = [0] * 1001


def dp(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        if d[n] != 0:
            return d[n]
        else:
            d[n] = dp(n - 1) + 2 * dp(n - 2)
            return d[n]


while True:
    try:
        N = int(sys.stdin.readline())
        print(dp(N))
    except:
        break
