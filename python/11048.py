# boj 11048
# blog : jjangsungwon.tistory.com

import sys

if __name__ == "__main__":

    # input
    N, M = map(int, input().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    dp = [[0] * M for _ in range(N)]
    dp[0][0] = arr[0][0]

    # 첫 줄
    for i in range(1, M):
        dp[0][i] = dp[0][i - 1] + arr[0][i]

    for i in range(1, N):
        for j in range(M):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + arr[i][j]
            else:
                dp[i][j] = max(max(dp[i - 1][j], dp[i - 1][j - 1]), dp[i][j - 1]) + arr[i][j]

    # print
    print(dp[N - 1][M - 1])
