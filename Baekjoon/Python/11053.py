import sys

if __name__ == "__main__":
    
    n = int(sys.stdin.readline())
    data_list = list(map(int, sys.stdin.readline().split()))
    
    dp = [1] * n
    
    for i in range(n):
        for j in range(i):
            if data_list[i] > data_list[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    print(max(dp))