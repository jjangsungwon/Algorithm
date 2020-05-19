if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())

        print(M * 2 - N, M - (M * 2 - N))