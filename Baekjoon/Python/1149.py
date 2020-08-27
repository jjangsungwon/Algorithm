# github : jjangsungwon.github.io

result = []
sum = 1000000000
# input
N = int(input())
R = 0
G = 1
B = 2

# 2차원 배열 생성
color = [list(map(int, input().split())) for _ in range(N)]
cost = [list(0 for _ in range(3)) for _ in range(N)]

cost[0][R] = color[0][R]
cost[0][G] = color[0][G]
cost[0][B] = color[0][B]

for i in range(1, N):
    cost[i][R] = min(color[i][R] + cost[i - 1][G], color[i][R] + cost[i - 1][B])
    cost[i][G] = min(color[i][G] + cost[i - 1][R], color[i][G] + cost[i - 1][B])
    cost[i][B] = min(color[i][B] + cost[i - 1][R], color[i][B] + cost[i - 1][G])

print(min(min(cost[N - 1][R], cost[N - 1][G]), cost[N - 1][B]))
