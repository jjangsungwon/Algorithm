if __name__ == "__main__":

    N = int(input())
    length = 0

    for i in range(1, 10):
        limit = int(str(9) * i)
        if N <= limit:
            length = 0
            temp = 9
            for j in range(1, i):
                length += temp * j
                temp *= 10
            length += i * (N - limit // 10)
            break
    print(length)

    """
    if N <= 9:
        length = N
    elif N <= 99:
        length = 9  # 1 ~ 9
        length += 2 * (N - 9) # 10 ~ 해당 숫자
    elif N <= 999:
        length = 9 + 180  # 1~9 + 10~99
        length += 3 * (N - 99)  # 100 ~ 해당 숫자
    elif N <= 9999:
        length = 9 + 180 + 2700
        length += 4 * (N - 999)
    elif N <= 99999:
        length = 9 + 180 + 2700 + 36000
        length += 5 * (N - 9999)
    elif N <= 999999:
        length = 9 + 180 + 2700 + 36000 + 450000
        length += 6 * (N - 99999)
    elif N <= 9999999:
        length = 9 + 180 + 2700 + 36000 + 450000 + 5400000
        length += 6 * (N - 999999)
    elif N <= 99999999:
        length = 9 + 180 + 2700 + 36000 + 450000 + 5400000 + 63000000
        length += 7 * (N - 9999999)
    elif N <= 999999999:
        length = 9 + 180 + 2700 + 36000 + 450000 + 5400000 + 63000000 + 720000000
        length += 8 * (N - 99999999)

    print(length)
    """