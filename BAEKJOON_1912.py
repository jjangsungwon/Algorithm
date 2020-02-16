N = int(input())
data = list(map(int, input().split()))

data.insert(0, 0)

real_max = 0
dp = list(0 for _ in range(100002))

dp[1] = data[1]

for i in range(2, N+1):
    dp[i] = max(dp[i-1] + data[i], data[i])

real_max = dp[1]

for i in range(1, N+1):
    if dp[i] > real_max:
        real_max = dp[i]

print(real_max)
