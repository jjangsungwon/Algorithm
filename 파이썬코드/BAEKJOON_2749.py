import sys


def fibonacci_pisano(n):
    fibo = [0, 1]
    mod = 1000000
    p = int(mod / 10 * 15) # 15 * 10^(k-1)
    i = 2
    while i < p:
        fibo.append(fibo[i - 1] + fibo[i - 2])
        fibo[i] %= mod
        i += 1
    return fibo[n % p]


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    print(fibonacci_pisano(N))
