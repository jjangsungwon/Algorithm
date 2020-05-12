if __name__ == "__main__":

    N = int(input())

    val = N // 5
    remain = N % 5

    if remain == 0:
        print(val)
    else:
        print(val + 1)