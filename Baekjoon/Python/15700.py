if __name__ == "__main__":

    N, M = map(int, input().split())

    total = 0

    # 2 * 1 채우기
    total += (M // 2) * N

    # 1 * 2 채우기
    if M % 2 != 0:
        total += (N // 2)

    print(total)