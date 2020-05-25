if __name__ == "__main__":

    N = int(input())

    if N % 2 == 1: # N이 홀수인 경우
        print(0)
    else:
        if N == 2:
            print(3)
        else:
            dp = [0] * (N // 2 + 1)
            dp[0] = 1

            for i in range(1, N // 2 + 1):
                dp[i] = dp[i - 1] * 3
                for j in range(i - 1):
                    dp[i] += dp[j] * 2
            print(dp[N // 2])
