if __name__ == "__main__":

    N = input()

    temp = 0
    val = 1
    for i in range(len(N) - 1, -1, -1):
        if N[i] == '1':
            temp += val

        val *= 2

    temp *= 17

    result = []
    while temp:
        result.insert(0, temp % 2)
        temp //= 2

    print("".join(map(str, result)))

