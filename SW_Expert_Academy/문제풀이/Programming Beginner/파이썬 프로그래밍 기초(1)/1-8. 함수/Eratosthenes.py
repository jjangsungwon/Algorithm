# 회문
import math


def Eratosthenes(n):
    is_primes = [True for _ in range(n+1)]
    length = math.ceil(math.sqrt(n)) + 1

    for i in range(2, length):
        if is_primes[i]:
            for j in range(i + i, n, i):
                is_primes[j] = False

    return [i for i in range(2, n + 1) if is_primes[i]]

num = int(input())
result = Eratosthenes(num)

for n in result:
    if n == num:
        print("소수입니다.")
