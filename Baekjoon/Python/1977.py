import math


if __name__ == "__main__":

    M = int(input())
    N = int(input())

    num = []
    for i in range(M, N + 1):
        if math.sqrt(i) % 1 == 0:
            num.append(i)

    if len(num) == 0:
        print(-1)
    else:
        print(sum(num))
        print(min(num))