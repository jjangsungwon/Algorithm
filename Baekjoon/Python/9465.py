if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        N = int(input())

        row = []
        for _ in range(2):
            row.append(list(map(int, input().split())))

        dp = [[0] * N for _ in range(2)]

        for i in range(2):
            dp[i][0], dp[i][1] = row[i][0], row[i][1]
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

        for j in range(2, N):
            dp[0][j] = row[0][j] + max(dp[1][j-1], dp[1][j-2])
            dp[1][j] = row[1][j] + max(dp[0][j - 1], dp[0][j - 2])

        max_val = -1
        max_val = max(max(max_val, max(dp[0])), max(dp[1]))
        print(max_val)

