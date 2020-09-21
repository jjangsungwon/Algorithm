import copy

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]


def change(array, x, y):  # 해당 위치와 상, 하, 좌, 우 스위치 반대로 전환
    for i in range(5):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 10 and 0 <= ny < 10:
            if array[nx][ny] == "#":
                array[nx][ny] = "O"
            else:
                array[nx][ny] = "#"


def check(array):  # 전구를 모두 껐는지 확인
    for i in range(10):
        for j in range(10):
            if array[i][j] == "O":
                return False
    return True


if __name__ == "__main__":
    maps = [list(input().strip()) for _ in range(10)]

    answer = 101
    for bitmask in range(0, (1 << 10)):  # bitmask를 통해서 첫 행의 스위치 모든 경우를 구현한다.
        copy_maps = copy.deepcopy(maps)
        cnt = 0
        for i in range(0, 10):
            if bitmask & (1 << i):
                change(copy_maps, 0, i)
                cnt += 1

        # 1 ~ 9행은 자기 위 행렬 값을 보고 스위치를 누를지 판단한다.
        for i in range(1, 10):
            for j in range(10):
                if copy_maps[i - 1][j] == "O":
                    change(copy_maps, i, j)
                    cnt += 1

        # 업데이트
        if check(copy_maps):
            answer = min(answer, cnt)

    if answer == 101:
        print(-1)
    else:
        print(answer)
