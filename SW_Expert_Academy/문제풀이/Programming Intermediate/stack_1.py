T = int(input())
d = [0 for _ in range(301)]


def dp(n):
    if n == 10:
        return 1
    elif n == 20:
        return 3
    else:
        d[n] = dp(n - 10) + dp(n - 20) * 2
        return d[n]


for i in range(1, T+1):
    data = int(input())
    print("#{0} {1}".format(i, dp(data)))
