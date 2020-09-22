import copy


INF = int(1e9)
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]


def change(array, x, y):
    for i in range(5):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if array[nx][ny] == 0:
                array[nx][ny] = 1
            else:
                array[nx][ny] = 0


if __name__ == "__main__":
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]

    # 초기에 모두 꺼져있는지 확인
    flag = True
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1:
                flag = False

    if flag:
        print(0)
    else:
        answer = INF
        for bitmask in range(int(pow(2, n) - 1), -1, -1):
            copy_maps = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    copy_maps[i][j] = maps[i][j]

            cnt = 0
            flag = True

            for k in range(n):
                if (1 << k) & bitmask:
                    cnt += 1
                    change(copy_maps, 0, k)

            for i in range(1, n):
                if flag:
                    for j in range(n):
                        if copy_maps[i - 1][j] == 1:
                            change(copy_maps, i, j)
                            cnt += 1
                            if cnt > answer:
                                flag = False
                                break
                else:
                    break

            if not flag:
                continue
            else:
                flag = True
                for i in range(n):
                    if copy_maps[n - 1][i] == 1:
                        flag = False
                if flag:
                    answer = min(answer, cnt)

        if answer == INF:
            print(-1)
        else:
            print(answer)



