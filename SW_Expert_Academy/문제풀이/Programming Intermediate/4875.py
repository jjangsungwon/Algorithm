T = int(input())

check = 0


def dfs(start_x, start_y, size, visited, data):
    global check
    if data[start_x][start_y] == 3:
        check = 1
        return

    # 상
    if start_x - 1 >= 0:
        if visited[start_x - 1][start_y] == 0 and data[start_x - 1][start_y] != 1:
            visited[start_x - 1][start_y] = 1
            dfs(start_x - 1, start_y, size, visited, data)

    # 하
    if start_x + 1 <= size:
        if visited[start_x + 1][start_y] == 0 and data[start_x + 1][start_y] != 1:
            visited[start_x + 1][start_y] = 1
            dfs(start_x + 1, start_y, size, visited, data)

    # 좌
    if start_y - 1 >= 0:
        if visited[start_x][start_y - 1] == 0 and data[start_x][start_y - 1] != 1:
            visited[start_x][start_y - 1] = 1
            dfs(start_x, start_y - 1, size, visited, data)

    # 우
    if start_y + 1 <= size:
        if visited[start_x][start_y + 1] == 0 and data[start_x][start_y + 1] != 1:
            visited[start_x][start_y + 1] = 1
            dfs(start_x, start_y + 1, size, visited, data)


for tc in range(1, T + 1):
    row = int(input())
    data = []
    start_x = 0
    start_y = 0
    check = 0
    visited = []

    # 지도 완성
    for i in range(row):
        temp = list(map(int, input()))
        data.append(temp)

        temp = [0] * len(temp)
        visited.append(temp)

    # 2의 위치 파악
    for i in range(row - 1, -1, -1):
        for j in range(len(data[i])):
            if data[i][j] == 2:
                start_x = i
                start_y = j
                break

    dfs(start_x, start_y, row - 1, visited, data)

    if check:
        print("#{0} 1".format(tc))
    else:
        print("#{0} 0".format(tc))
