if __name__ == "__main__":

    T = int(input())

    for i in range(T):
        N, M = map(int, input().split())

        result = 1

        if N == M:
            print(1)
        else:
            for i in range(M, M - N, -1):
                result *= i

            for i in range(N, 1, -1):
                result //= i

            print(result)
