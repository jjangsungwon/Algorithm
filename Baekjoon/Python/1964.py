if __name__ == "__main__":

    N = int(input())

    result, val = 5, 7
    if N == 1:
        print(result)
    else:
        for i in range(N - 1):
            result += val
            val += 3

        print(result % 45678)