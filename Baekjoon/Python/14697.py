if __name__ == "__main__":

    A, B, C, N = map(int, input().split())

    for i in range(N // A + 1):
        for j in range(N // B + 1):
            for k in range(N // C + 1):
                if A * i + B * j + C * k == N:
                    print(1)
                    exit()
    print(0)