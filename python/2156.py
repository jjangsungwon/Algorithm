import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    data = [0]
    dp = [0 for _ in range(N + 1)]

    for _ in range(N):
        data.append(int(sys.stdin.readline()))

    for i in range(1, N + 1):
        if i == 1:
            dp[1] = data[1]
        elif i == 2:
            dp[2] = data[1] + data[2]
        else:
            dp[i] = max(dp[i-3] + data[i-1] + data[i], dp[i-2] + data[i], dp[i-1])

    print(dp[N])