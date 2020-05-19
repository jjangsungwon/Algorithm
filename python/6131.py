if __name__ == "__main__":

    N = int(input())

    cnt = 0
    for i in range(1, 500):
        for j in range(1, i):
            if i * i == j * j + N:
                 cnt += 1
    print(cnt)
