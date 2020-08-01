import sys


if __name__ == "__main__":

    # input
    N = int(input())
    M = int(input())
    bus = [list(map(int, input().split())) for _ in range(M)]

    d = [[sys.maxsize] * N for _ in range(N)]

    # initial
    for row, col, cost in bus:
        d[row - 1][col - 1] = min(d[row - 1][col - 1], cost)
    for i in range(N):
        d[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    for i in range(N):
        for j in range(N):
            if d[i][j] == sys.maxsize:
                d[i][j] = 0

    for i in range(N):
        print(" ".join(map(str, d[i])))