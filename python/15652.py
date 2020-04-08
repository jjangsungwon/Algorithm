# BOJ 15652
# github blog : jjangsungwon.github.io

import itertools

if __name__ == "__main__":
    N, M = map(int, input().split())

    data = [i for i in range(1, N + 1)]
    result = itertools.combinations_with_replacement(data, M)

    for i in result:
        print(" ".join(map(str, i)))