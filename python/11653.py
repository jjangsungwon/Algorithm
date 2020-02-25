import sys
import math


def get_primes(n):
    is_primes = [1] * (n+1)
    # n의 최대 약수가 sqrt(n) 이하임
    max_length = math.ceil(math.sqrt(n))

    for i in range(2, max_length):
        if is_primes[i]:
            for j in range(i + i, n, i):
                is_primes[j] = False

    # 리스트의 True로 남아 있는 인덱스(소수)를 추출
    return [i for i in range(2, n+1) if is_primes[i]]


def get_factorization(num):
    factors = []
    for prime in get_primes(num):
        count = 0
        while num % prime == 0:
            num /= prime
            count += 1
            factors.append(prime)
    return factors


N = int(sys.stdin.readline())
result = get_factorization(N)

for i in range(len(result)):
    print(result[i])