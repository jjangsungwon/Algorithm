def dfs(cnt, row, col):
    global max_cnt

    for i in range(4):
        y, x = row + dy[i], col + dx[i]
        if 0 <= y < R and 0 <= x < C and data[y][x]:
            value = ord(data[y][x]) - ord('A')
            if not check[value]:
                check[value] = True
                dfs(cnt + 1, y, x)
                check[value] = False

    max_cnt = max(max_cnt, cnt)


if __name__ == "__main__":

    R, C = map(int, input().split())
    data = []

    for _ in range(R):
        data.append(list(input().strip()))

    max_cnt = 0
    check = [False] * 26
    check[ord(data[0][0]) - ord('A')] = True

    # 상 하 좌 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    dfs(1, 0, 0)

    print(max_cnt)
