import sys
from collections import deque

zero_cnt = 0


def bfs(p):
    global zero_cnt
    visited = [[0] * M for _ in range(N)]
    q = deque(p)

    cnt = 0
    while zero_cnt:
        temp = []
        while q:
            row, col = q.popleft()

            # 상
            if row - 1 >= 0 and tomato[row - 1][col] == 0 and not visited[row - 1][col]:
                visited[row - 1][col] = 1
                tomato[row - 1][col] = 1
                temp.append([row - 1, col])
                zero_cnt -= 1

            # 하
            if row + 1 < N and tomato[row + 1][col] == 0 and not visited[row + 1][col]:
                visited[row + 1][col] = 1
                tomato[row + 1][col] = 1
                temp.append([row + 1, col])
                zero_cnt -= 1

            # 좌
            if col - 1 >= 0 and tomato[row][col - 1] == 0 and not visited[row][col - 1]:
                visited[row][col - 1] = 1
                tomato[row][col - 1] = 1
                temp.append([row, col - 1])
                zero_cnt -= 1

            # 우
            if col + 1 < M and tomato[row][col + 1] == 0 and not visited[row][col + 1]:
                visited[row][col + 1] = 1
                tomato[row][col + 1] = 1
                temp.append([row, col + 1])
                zero_cnt -= 1

        cnt += 1
        q.extend(temp)

        if len(q) == 0 and zero_cnt != 0:
            return -1
    return cnt


if __name__ == "__main__":

    M, N = map(int, input().split())
    tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 토마토 위치 받아오기
    position = []
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                position.append([i, j])
            elif tomato[i][j] == 0:
                zero_cnt += 1

    print(bfs(position))
