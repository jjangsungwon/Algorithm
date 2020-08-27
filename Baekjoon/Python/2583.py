# boj 2583
# blog : jjangsungwon.tistory.com
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(row, col):
    global answer
    answer += 1
    # 상
    if row - 1 >= 0 and arr[row - 1][col] == 0:
        arr[row - 1][col] = 1
        dfs(row - 1, col)
    # 하
    if row + 1 < M and arr[row + 1][col] == 0:
        arr[row + 1][col] = 1
        dfs(row + 1, col)

    # 좌
    if col - 1 >= 0 and arr[row][col - 1] == 0:
        arr[row][col - 1] = 1
        dfs(row, col - 1)

    # 우
    if col + 1 < N and arr[row][col + 1] == 0:
        arr[row][col + 1] = 1
        dfs(row, col + 1)


if __name__ == "__main__":

    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * N for _ in range(M)]

    # 사각형 입력 받기
    for _ in range(K):
        bottom_x, bottom_y, top_x, top_y = map(int, sys.stdin.readline().split())

        for i in range(bottom_y, top_y):
            for j in range(bottom_x, top_x):
                arr[i][j] = 1

    area, cnt = [], 0
    # 사각형 개수 및 넓이 구하기
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 0:
                arr[i][j] = 1
                answer = 0
                dfs(i, j)
                area.append(answer)
                cnt += 1  # dfs 들어간 횟수만큼 영역 존재

    area.sort()
    print(cnt)
    print(" ".join(map(str, area)))
