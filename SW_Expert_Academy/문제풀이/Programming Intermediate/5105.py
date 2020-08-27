min_count = 10000


def range_check(y, x):
    return 0 <= y < N and 0 <= x < N and (Maze[y][x] == 0 or Maze[y][x] == 3)


def bfs(start_y, start_x):
    global min_count
    Q.append((start_y, start_x))
    visited.append((start_y, start_x))

    while Q:
        start_y, start_x = Q.pop(0)
        for dir in range(4):
            new_y = start_y + dy[dir]
            new_x = start_x + dx[dir]
            if range_check(new_y, new_x) and (new_y, new_x) not in visited:
                Q.append((new_y, new_x))
                visited.append((new_y, new_x))
                count[new_y][new_x] = count[start_y][start_x] + 1

                if Maze[new_y][new_x] == 3:
                    min_count = count[new_y][new_x] - 1
                    return


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]
    visited = []
    count = [[0] * N for _ in range(N)]

    # 출발지 찾기
    for y in range(N):
        for x in range(N):
            if Maze[y][x] == 2:
                start_y, start_x = y, x

    # 상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    min_count = 0
    Q = []

    bfs(start_y, start_x)
    print('#{0} {1}'.format(tc, min_count))
