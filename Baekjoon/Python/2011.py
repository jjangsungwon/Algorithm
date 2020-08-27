if __name__ == "__main__":

    N = input()
    dp = [0] * (len(N) + 1)

    dp[0], dp[1] = 1, 1

    if N[0] == '0':
        print(0)
    else:
        for i in range(2, len(N) + 1):
            if int(N[i-1]) > 0:
                dp[i] = dp[i-1]

            if 10 <= int(N[i-2] + N[i-1]) <= 26:
                dp[i] += dp[i-2]

        print(dp[len(N)] % 1000000)