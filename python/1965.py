if __name__ == "__main__":

    N = int(input())
    data = list(map(int, input().split()))
    dp = [1] * len(data)

    for i in range(len(data)):
        for j in range(i):
            if data[i] > data[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))
