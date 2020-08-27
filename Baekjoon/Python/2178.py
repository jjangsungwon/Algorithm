from collections import deque
import sys


def bfs(row, col):
    q = deque([[row, col]])
    visited = [[0] * M for _ in range(N)]

    cnt = 1
    while True:
        temp = []
        while q:
            new_row, new_col = q.popleft()

            if new_row == N - 1 and new_col == M - 1:
                return cnt
            # 상
            if new_row - 1 >= 0 and arr[new_row - 1][new_col] == 1 and not visited[new_row - 1][new_col]:
                temp.append([new_row - 1, new_col])
                visited[new_row - 1][new_col] = 1

            # 하
            if new_row + 1 < N and arr[new_row + 1][new_col] == 1 and not visited[new_row + 1][new_col]:
                temp.append([new_row + 1, new_col])
                visited[new_row + 1][new_col] = 1

            # 좌
            if new_col - 1 >= 0 and arr[new_row][new_col - 1] == 1 and not visited[new_row][new_col - 1]:
                temp.append([new_row, new_col - 1])
                visited[new_row][new_col - 1] = 1

            # 우
            if new_col + 1 < M and arr[new_row][new_col + 1] == 1 and not visited[new_row][new_col + 1]:
                temp.append([new_row, new_col + 1])
                visited[new_row][new_col + 1] = 1
        cnt += 1
        q.extend(temp)


if __name__ == "__main__":
    # input
    N, M = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

    print(bfs(0, 0))
