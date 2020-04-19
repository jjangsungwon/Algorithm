import math
import sys


def prime(n):  # n보다 같거나 홀수 소수 구하기
    primes = [1] * (n + 1)
    max_length = int(math.sqrt(n)) + 1

    for i in range(2, max_length):
        if primes[i]:
            for j in range(i + i, n, i):
                primes[j] = False
    return primes


if __name__ == "__main__":
    primes = prime(1000000)

    while True:
        N = int(sys.stdin.readline())

        if N == 0:
            break

        for i in range(2, N):
            if primes[i] and primes[N - i]:
                print("{0} = {1} + {2}".format(N, i, N - i))
                break
