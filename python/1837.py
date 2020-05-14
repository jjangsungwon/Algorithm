import math


def era(N):  # N 범위까지의 소수 구하기

    temp = [True] * (N + 1)
    for i in range(2, int(math.sqrt(N)) + 1):
        if temp[i]:
            for j in range(i + i, N + 1, i):
                temp[j] = False
    return [i for i in range(2, N + 1) if temp[i]]


if __name__ == "__main__":

    # input
    P, K = map(int, input().split())
    prime = era(K)

    for i in prime:
        if P % i == 0:
            print("BAD", min(i, P // i))
            exit(0)
    print("GOOD")
