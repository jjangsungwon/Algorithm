import itertools


if __name__ == "__main__":

    N = int(input())
    data = [i for i in range(1, N + 1)]
    result = list(itertools.permutations(data, N))

    for data in result:
        print(" ".join(map(str, data)))
