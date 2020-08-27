import sys

money = int(sys.stdin.readline())
data = [500, 100, 50, 10, 5, 1]

money = 1000 - money
count = 0

for i in range(len(data)):
    while money - data[i] >= 0:
        money -= data[i]
        count += 1

print(count)
