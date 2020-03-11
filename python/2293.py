import sys

if __name__ == "__main__":
    
    n, k = map(int, input().split())
    data_list = []
    dp = [0 for _ in range(k + 1)]
    
    for i in range(n):
        data_list.append(int(input()))
        
    dp[0] = 1
    for i in data_list:
        for j in range(i, k+1):
            dp[j] += dp[j-i]
    
    print(dp[k])