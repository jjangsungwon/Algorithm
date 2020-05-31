# boj 11057
# blog : jjangsungwon.tistory.com


if __name__ == "__main__":

    # input
    N = int(input())

    if N == 1:
        print(10)
    else:
        dp = [[0] * 10 for _ in range(N)]

        for i in range(10):
            dp[0][i] = i + 1

        for i in range(1, N):
            for j in range(10):
                dp[i][j] = sum(dp[i - 1][:j + 1])

        print(dp[N - 1][9] % 10007)