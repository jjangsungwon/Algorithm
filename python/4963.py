dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]


def bfs(i, j):
    global cnt, n
    visited[i][j] = 1

    q = []
    q.append((i, j))

    while q:
        current = q.pop(0)

        for k in range(8):
            y = current[0] + dy[k]
            x = current[1] + dx[k]

            if 0 <= y < h and 0 <= x < w:
                if visited[y][x] == 0 and m[y][x] == "1":
                    q.append((y, x))
                    visited[y][x] = 1


if __name__ == "__main__":

    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        m = []
        visited = [[0] * w for _ in range(h)]
        cnt = 0
        for i in range(h):
            temp = list(input().split())
            m.append(temp)

        for i in range(h):
            for j in range(w):
                if m[i][j] == "1" and visited[i][j] == 0:
                    bfs(i, j)
                    cnt += 1

        print(cnt)
