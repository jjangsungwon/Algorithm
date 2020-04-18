if __name__ == "__main__":

    first_string = list(input().strip())
    second_string = list(input().strip())

    dp = [[0] * (len(second_string) + 1) for _ in range(len(first_string) + 1)]

    for i in range(1, len(first_string) + 1):
        for j in range(1, len(second_string) + 1):
            if first_string[i - 1] == second_string[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[-1][-1])
