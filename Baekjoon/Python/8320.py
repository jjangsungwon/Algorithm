import math


if __name__ == "__main__":

    N = int(input())
    total = 0

    for i in range(1, math.floor(math.sqrt(N)) + 1):
        for j in range(i * i, N + 1, i):
            total += 1
    print(total)
