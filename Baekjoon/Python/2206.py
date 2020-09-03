import sys
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = []
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]  # 벽을 부순거랑, 부수지 않은 거 상황을 구분해야 한다.
    heapq.heappush(q, (1, 0, 0, 0))  # 거리, x, y, flag(벽)
    visited[0][0][0] = True

    while q:  # q가 빌 떄까지 반복
        cnt, x, y, flag = heapq.heappop(q)
        if x == n - 1 and y == m - 1:  # 목표 지점 도달
            return cnt
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if array[nx][ny] == 0:  # 빈칸
                    if visited[nx][ny][flag] == 0:
                        visited[nx][ny][flag] = 1
                        heapq.heappush(q, (cnt + 1, nx, ny, flag))
                elif array[nx][ny] == 1:
                    if not flag and visited[nx][ny][True] == 0:
                        visited[nx][ny][flag] = 1
                        heapq.heappush(q, (cnt + 1, nx, ny, True))
    return -1


if __name__ == "__main__":
    n, m = map(int, input().split())  # 맵의 크기 입력받기
    array = [list(map(int, input().strip())) for _ in range(n)]

    # bfs 탐색
    answer = 1e9
    answer = bfs()

    print(answer)
