if __name__ == "__main__":
    area = [[0] * 100 for _ in range(100)]

    T = int(input()) #  test case
    coordinate = []
    for _ in range(T):
        coordinate.append((list(map(int, input().split()))))

    cnt = 0
    for i in range(len(coordinate)):
        start_row = coordinate[i][0]
        start_col = coordinate[i][1]

        for i in range(start_row, start_row + 10):
            for j in range(start_col, start_col + 10):
                if area[i][j] == 0:
                    area[i][j] = 1
                    cnt += 1
    print(cnt)