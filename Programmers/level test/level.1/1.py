import math

def solution(n):
    primes = [True] * (n+1)
    max_length = math.ceil(math.sqrt(n))

    for i in range(2, max_length):
        if primes[i]:
            for j in range(i + i, n+1, i):
                primes[j] = False

    return len([i for i in range(2, n+1) if primes[i]])