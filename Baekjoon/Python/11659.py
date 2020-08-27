import sys


if __name__ == "__main__":

    N, M = map(int, input().split())
    num_list = list(map(int, sys.stdin.readline().split()))
    dp = [0] * len(num_list)
    dp[0] = num_list[0]

    for i in range(1, len(num_list)):
        dp[i] = dp[i - 1] + num_list[i]

    for _ in range(M):
        i, j = map(int, input().split())
        result = dp[j - 1] - dp[i - 1] + num_list[i - 1]
        print(result)