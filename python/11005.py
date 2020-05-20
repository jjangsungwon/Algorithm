if __name__ == "__main__":
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    N, B = map(int, input().split())

    result = ""

    while N != 0:
        val = N % B
        if val >= 10:
            result = alpha[val - 10] + result
        else:
            result = str(val) + result
        N //= B
    print(result)
