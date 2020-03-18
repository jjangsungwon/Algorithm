def dp(n):
    if n <= 2:
        d[n] = 1
        return d[n]
    else:
        if d[n] != 0:
            return d[n]
        else:
            d[n] = dp(n - 2) + dp(n - 1)
            return d[n]


if __name__ == "__main__":
    N = int(input())
    d = [0 for _ in range(N + 1)]

    dp(N)

    print(d[N])
