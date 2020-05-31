# boj 2294
# blog : jjangsungwon.tistory.com
import sys


if __name__ == "__main__":

    n, k = map(int, input().split())
    coin = [int(sys.stdin.readline()) for _ in range(n)]

    coin = list(set(coin))
    coin.sort()

    dp = [sys.maxsize] * (k + 1)

    for i in range(1, k + 1):
        if i in coin:  # 동전 1개로 가능한 경우
            dp[i] = 1
        else:
            for j in coin:
                if i - j >= 0:
                    dp[i] = min(dp[i - j] + 1, dp[i])

    if dp[k] == sys.maxsize:
        print(-1)
    else:
        print(dp[k])
