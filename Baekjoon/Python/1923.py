
if __name__ == "__main__":
    
    n = int(input())
    data = []
    
    for i in range(n):
        temp = list(map(int, input().split()))
        data.append(temp)
    
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = data[0][0]
    
    for i in range(1, n):
        for j in range(len(data[i])):
            dp[i][j] = max(dp[i-1][j] + data[i][j], dp[i-1][j-1] + data[i][j])
    
    print(max(dp[n-1]))