import sys
from collections import deque

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(r, c):
    q = deque([[r, c, 0]])
    visited = {(r, c)}

    while True:
        r, c, cnt = q.popleft()
        for i in range(4):
            new_row, new_col = r + dy[i], c + dx[i]
            if 0 <= new_row < row and 0 <= new_col < col and arr[new_row][new_col] == "L" and (new_row, new_col) not in visited:
                q.append([new_row, new_col, cnt + 1])
                visited.add((new_row, new_col))
        if len(q) == 0:
            return cnt


if __name__ == "__main__":

    # input
    row, col = map(int, sys.stdin.readline().split())
    arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(row)]

    answer = -1
    for i in range(row):
        for j in range(col):
            if arr[i][j] == "L":
                answer = max(answer, bfs(i, j))
    print(answer)