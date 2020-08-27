if __name__ == "__main__":
    data = []
    cnt = 0

    # input
    for _ in range(8):
        data.append(list(map(str, input().strip())))

    for i in range(8):
        for j in range(8):
            if i % 2 == 0 and j % 2 == 0 and data[i][j] == 'F':
                cnt += 1
            elif i % 2 == 1 and j % 2 == 1 and data[i][j] == 'F':
                cnt += 1

    print(cnt)