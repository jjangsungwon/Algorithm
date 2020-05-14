if __name__ == "__main__":

    N, M = map(int, input().split())

    # N 좌표 구하기
    if N % 4 == 1:
        N = [0, N // 4]
    elif N % 4 == 2:
        N = [1, N // 4]
    elif N % 4 == 3:
        N = [2, N // 4]
    else:
        N = [3, N // 4 - 1]

    # M 좌표 구하기
    if M % 4 == 1:
        M = [0, M // 4]
    elif M % 4 == 2:
        M = [1, M // 4]
    elif M % 4 == 3:
        M = [2, M // 4]
    else:
        M = [3, M // 4 - 1]

    print(abs(M[0] - N[0]) + abs(M[1] - N[1]))
