import sys
data = list(map(int, sys.stdin.readline().split()))
pow_sum = 0

for num in data:
    pow_sum += num * num

pow_sum %= 10

print(pow_sum)