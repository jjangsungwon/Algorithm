if __name__ == "__main__":

    N = int(input())

    data = list(map(int, input().split()))

    for _ in range(N - 1):
        temp = sorted(list(map(int, input().split())) + data, reverse=True)
        data = temp[:N]

    print(data[N-1])
