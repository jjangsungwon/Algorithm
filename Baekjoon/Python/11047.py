import sys

N, K = map(int, sys.stdin.readline().split())
data = []
for i in range(N):
    data.append(sys.stdin.readline())

total = 0
count = 0

for i in range(len(data) - 1, -1, -1):
    if total + int(data[i]) <= K:
        while True:
            total += int(data[i])
            count += 1

            if total + int(data[i]) > K:
                break

    if total == K:
        print(count)
        break
