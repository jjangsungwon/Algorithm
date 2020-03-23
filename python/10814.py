if __name__ == "__main__":

    N = int(input())
    data = []

    for i in range(N):
        data.append(input().split())

    data = sorted(data, key=lambda x: int(x[0]))

    for i in range(N):
        print(" ".join(map(str, data[i])))
