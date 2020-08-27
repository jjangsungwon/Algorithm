if __name__ == "__main__":

    N = int(input())
    length = 0

    for i in range(1, N + 1):
        length += len(str(i))

    print(length)
