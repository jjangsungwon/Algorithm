from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(board):
    length = len(board)
    q = deque()
    q.append((0, 0, 0, -1))  # 비용, 위치, 방향(-1 - 가로, 1 - 세로)
    q.append((0, 0, 0, 1))
    visited = dict()
    visited[(0, 0)] = 0

    answer = sys.maxsize
    while q:
        cost, x, y, dir = q.popleft()
        if x == length - 1 and y == length - 1:
            answer = min(answer, cost)
            continue

        # 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < length and 0 <= ny < length and board[nx][ny] == 0:
                if (nx, ny) not in visited:
                    if dir == 1:
                        if i == 0 or i == 1:
                            q.append((cost + 100, nx, ny, dir))
                            visited[(nx, ny)] = cost + 100
                        else:
                            q.append((cost + 600, nx, ny, -dir))
                            visited[(nx, ny)] = cost + 600
                    else:
                        if i == 0 or i == 1:
                            q.append((cost + 600, nx, ny, -dir))
                            visited[(nx, ny)] = cost + 600
                        else:
                            q.append((cost + 100, nx, ny, dir))
                            visited[(nx, ny)] = cost + 100
                else:
                    if dir == 1:
                        if (i == 0 or i == 1) and visited[(nx, ny)] >= (cost + 100):
                            visited[(nx, ny)] = cost + 100
                            q.append((cost + 100, nx, ny, dir))
                        elif (i == 2 or i == 3) and visited[(nx, ny)] >= (cost + 600):
                            visited[(nx, ny)] = cost + 600
                            q.append((cost + 600, nx, ny, -dir))
                    else:
                        if (i == 0 or i == 1) and visited[(nx, ny)] >= (cost + 600):
                            visited[(nx, ny)] = cost + 600
                            q.append((cost + 600, nx, ny, -dir))
                        elif (i == 2 or i == 3) and visited[(nx, ny)] >= (cost + 100):
                            visited[(nx, ny)] = cost + 100
                            q.append((cost + 100, nx, ny, dir))

    return answer


def solution(board):
    return bfs(board)


if __name__ == "__main__":
    print(solution(
        [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
