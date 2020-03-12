
if __name__ == "__main__":
    
    n = int(input())
    data_list = list(map(int, input().split()))
    dp = [0] * (n + 1)
    
    for i in range(n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], dp[i-j] + data_list[j-1])
    
    print(dp[n])