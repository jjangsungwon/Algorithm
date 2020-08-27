import sys


if __name__ == "__main__":

    N = int(input())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    dp = [[0] * len(arr) for _ in range(len(arr))]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if i == N - 1 and j == N - 1:
                break
            value = arr[i][j]
            down = i + value
            right = j + value

            if down < N:
                dp[down][j] += dp[i][j]
            if right < N:
                dp[i][right] += dp[i][j]

    print(dp[len(arr) - 1][len(arr) - 1])