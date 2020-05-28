if __name__ == "__main__":
    N = int(input())
    dp = [[0] * 2 for _ in range(N)]

    if N == 1:
        print(3)
        exit(0)

    dp[0][0], dp[0][1] = 2, 3
    dp[1][0], dp[1][1] = 5, 7

    for i in range(2, N):
        for j in range(2):
            if j == 0:
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % 9901
            else:
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1]) % 9901

    print(dp[N - 1][1] % 9901)
