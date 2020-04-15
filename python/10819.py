import itertools


if __name__ == "__main__":

    N = int(input())
    data = list(map(int, input().split()))

    data = list(itertools.permutations(data, N))
    max_total = -99999999

    for i in range(len(data)):
        total = 0

        for j in range(len(data[i])-1):
            total += abs(data[i][j+1] - data[i][j])

        max_total = max(max_total, total)

    print(max_total)