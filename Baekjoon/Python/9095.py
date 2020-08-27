import sys

T = int(sys.stdin.readline())
data = []
for i in range(T):
    data.append(int(sys.stdin.readline()))

d = [0 for _ in range(100)]


def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        if d[n] != 0:
            return d[n]
        else:
            d[n] = dp(n - 1) + dp(n - 2) + dp(n - 3)
            return d[n]


for i in range(T):
    print(dp(data[i]))
