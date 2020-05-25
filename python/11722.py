if __name__ == "__main__":

    N = int(input())
    num_list = list(map(int, input().split()))
    dp = [1] * N
    dp[0] = 1

    for i in range(1, N):
        for j in range(i):
            if num_list[i] < num_list[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))