import math


if __name__ == "__main__":

    N = int(input())
    num = list(map(int, input().split()))
    divisor = []

    for i in range(1, int(math.sqrt(num[0])) + 1):
        if num[0] % i == 0:
            divisor.append(i)
            divisor.append(num[0] // i)

    divisor = set(divisor)
    for i in range(1, len(num)):
        next_divisor = []
        for j in range(1, int(math.sqrt(num[i])) + 1):
            if num[i] % j == 0:
                next_divisor.append(j)
                next_divisor.append(num[i] // j)

        next_divisor = set(next_divisor)
        divisor = set.intersection(divisor, next_divisor)

    divisor = list(divisor)
    divisor.sort()
    for i in range(len(divisor)):
        print(divisor[i])

