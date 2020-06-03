# boj 10026
# blog : jjangsungwon.tistory.com
import sys, copy
sys.setrecursionlimit(10 ** 6)


# 색약 x
def dfs(row, col):
    val = arr[row][col]  # 해당 값 저장
    arr[row][col] = 0

    # 상
    if row - 1 >= 0 and arr[row - 1][col] == val:
        dfs(row - 1, col)

    # 하
    if row + 1 < N and arr[row + 1][col] == val:
        dfs(row + 1, col)

    # 좌
    if col - 1 >= 0 and arr[row][col - 1] == val:
        dfs(row, col - 1)

    # 우
    if col + 1 < N and arr[row][col + 1] == val:
        dfs(row, col + 1)


def dfs2(row, col):
    val = arr[row][col]  # 해당 값 저장
    arr[row][col] = 0

    if val == "B":
        # 상
        if row - 1 >= 0 and arr[row - 1][col] == val:
            dfs2(row - 1, col)

        # 하
        if row + 1 < N and arr[row + 1][col] == val:
            dfs2(row + 1, col)

        # 좌
        if col - 1 >= 0 and arr[row][col - 1] == val:
            dfs2(row, col - 1)

        # 우
        if col + 1 < N and arr[row][col + 1] == val:
            dfs2(row, col + 1)
    else:
        # 상
        if row - 1 >= 0 and (arr[row - 1][col] == "R" or arr[row - 1][col] == "G"):
            dfs2(row - 1, col)

        # 하
        if row + 1 < N and (arr[row + 1][col] == "R" or arr[row + 1][col] == "G"):
            dfs2(row + 1, col)

        # 좌
        if col - 1 >= 0 and (arr[row][col - 1] == "R" or arr[row][col - 1] == "G"):
            dfs2(row, col - 1)

        # 우
        if col + 1 < N and (arr[row][col + 1] == "R" or arr[row][col + 1] == "G"):
            dfs2(row, col + 1)


if __name__ == "__main__":

    N = int(input())
    arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
    cnt_1, cnt_2 = 0, 0

    copy_arr = copy.deepcopy(arr)

    # 적록색약 x
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                dfs(i, j)
                cnt_1 += 1

    arr = copy.deepcopy(copy_arr)
    # 적록색약 o
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                dfs2(i, j)
                cnt_2 += 1

    print(cnt_1, cnt_2)
