if __name__ == "__main__":

    num = []
    N, M = map(int, input().split())
    for _ in range(N):
        num.append(list(map(int, input().split())))

    K = int(input())
    for _ in range(K):
        i, j, x, y = map(int, input().split())

        total = 0
        for k in range(i - 1, x):
            total += sum(num[k][j - 1:y])
        print(total)