import math


def era(n):  # n이하 소수 구하기
    length = int(math.sqrt(n)) + 1
    temp = [1] * (n + 1)
    for i in range(2, length):
        if temp[i]:
            for j in range(i + i, length, i):
                temp[i] = False
    return [i for i in range(2, len(temp)) if temp[i]]


if __name__ == "__main__":

    K, L = map(int, input().split())
    prime = era(L)

    flag = True
    for i in prime:
        if K % i == 0 and i < L:
            print("BAD", i)
            exit()
    print("GOOD")