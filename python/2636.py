from collections import deque


def division_bfs():
    q = deque([[0, 0]])
    visited = {(0, 0)}

    while q:
        row, col = q.popleft()

        for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상, 하, 좌, 우
            new_row, new_col = row + r, col + c
            if 0 <= new_row < y and 0 <= new_col < x:
                if arr[new_row][new_col] == 0 or arr[new_row][new_col] == -1 and (new_row, new_col) not in visited:
                    arr[new_row][new_col] = -1
                    q.append([new_row, new_col])
                    visited.add((new_row, new_col))


def bfs():
    change, temp = [], []
    while cheese:
        row, col = cheese.popleft()
        if arr[row - 1][col] == -1 or arr[row + 1][col] == -1 or arr[row][col - 1] == -1 or arr[row][col + 1] == -1:
            change.append([row, col])
        else:
            temp.append([row, col])

    cheese.extend(temp)
    if len(cheese) > 0:
        for r, c in change:
            arr[r][c] = -1
        return 1
    return 0


if __name__ == "__main__":
    # input
    y, x = map(int, input().split())  # 세로, 가로
    arr = [list(map(int, input().split())) for _ in range(y)]

    # 치즈 리스트 생성
    cheese = deque([])
    for i in range(y):
        for j in range(x):
            if arr[i][j] == 1:  # 치즈가 있으면
                cheese.append([i, j])

    time, area = 0, len(cheese)
    while cheese:
        time += 1
        # 외부와 내부 0 구분
        division_bfs()
        bfs()
        if len(cheese) != 0:
            area = len(cheese)

    print(time)
    print(area)
