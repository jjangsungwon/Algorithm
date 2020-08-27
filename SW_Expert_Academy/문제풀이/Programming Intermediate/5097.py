def reculer(N, M):
    M = M % N

    for i in range(M):
        n = data[0]
        data.pop(0)
        data.append(n)


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        data = list(map(int, input().split()))

        reculer(N, M)
        print("#{0} {1}".format(tc, data[0]))