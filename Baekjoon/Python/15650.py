import itertools

if __name__ == "__main__":
    N, M = map(int, input().split())
    temp = [i for i in range(1, N + 1)]

    data = list(itertools.combinations(temp, M))

    for i in range(len(data)):
        print(' '.join(map(str, data[i])))