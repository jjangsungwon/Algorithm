if __name__ == "__main__":

    N = int(input())
    data = list(map(int, input().split()))

    dp = [1] * N
    dp_re = [1] * N
    cnt = 0

    # 증가하는 수열
    for i in range(N):
        for j in range(i):
            if data[i] > data[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # 감소하는 수열
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, i, - 1):
            if data[i] > data[j]:
                dp_re[i] = max(dp_re[i], dp_re[j] + 1)

    max_val = -1
    for i in range(N):
        max_val = max(dp[i] + dp_re[i] -1, max_val)

    print(max_val)

