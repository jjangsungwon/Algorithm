import sys


def knapsack():
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            weight = pack[i][0]
            value = pack[i][1]

            if j < weight:
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = max(value + arr[i - 1][j - weight], arr[i - 1][j])


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    pack = [[0, 0]]

    # 입력
    for i in range(N):
        pack.append(list(map(int, sys.stdin.readline().split())))

    # arr
    arr = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    knapsack()

    print(arr[N][K])