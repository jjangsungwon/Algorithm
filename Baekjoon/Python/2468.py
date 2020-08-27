# boj 2468
# blog: jjangsungwon.tistory.com
import copy
import sys

sys.setrecursionlimit(10 ** 6)


def dfs(row, col):
    # 상
    if row - 1 >= 0 and arr[row - 1][col] == 1:
        arr[row - 1][col] = 0
        dfs(row - 1, col)
    # 하
    if row + 1 < N and arr[row + 1][col] == 1:
        arr[row + 1][col] = 0
        dfs(row + 1, col)

    # 좌
    if col - 1 >= 0 and arr[row][col - 1] == 1:
        arr[row][col - 1] = 0
        dfs(row, col - 1)

    # 우
    if col + 1 < N and arr[row][col + 1] == 1:
        arr[row][col + 1] = 0
        dfs(row, col + 1)


if __name__ == "__main__":

    N = int(input())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 물의 높이 범위
    min_height, max_height = sys.maxsize, - 1

    for i in range(N):
        min_height = min(min_height, min(arr[i]))
        max_height = max(max_height, max(arr[i]))

    original_arr = copy.deepcopy(arr)
    cnt = -1
    # 가능한 물 높이 모두 시행
    for k in range(min_height, max_height + 1):
        arr = copy.deepcopy(original_arr)

        # 잠기는 위치 확인
        for i in range(N):
            for j in range(N):
                if arr[i][j] <= k:
                    arr[i][j] = 0  # 물에 잠김
                else:
                    arr[i][j] = 1  # 물에 잠기지 않음

        count = 0
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 1:
                    dfs(i, j)
                    count += 1
        cnt = max(cnt, count)

    if cnt == 0:  # 비가 내리지 않은 경우 1개의 안전 영역 존재재
        print(1)
    else:
        print(cnt)
