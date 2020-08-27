import math


if __name__ == "__main__":

    N = int(input())
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        dp[i] = i  # 1로 채운 경우
        for j in range(1, i):
            if (j * j) > i:
                break
            dp[i] = min(dp[i], dp[i - j * j] + 1)

    print(dp[N])