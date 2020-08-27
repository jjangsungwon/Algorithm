import sys
from collections import deque


def bfs():

    position = deque()  # 이동 경로
    water = deque()  # 물의 위치
    for i in range(R):
        for j in range(C):
            if arr[i][j] == "*":
                water.append([i, j])
            elif arr[i][j] == "S":
                position.append([i, j])

    cnt = 1
    while True:

        # 물 업데이트
        length = len(water)
        for i in range(length):
            row, col = water.popleft()
            if row - 1 >= 0 and arr[row - 1][col] == ".":  # 상
                arr[row - 1][col] = "*"
                water.append([row - 1, col])
            if row + 1 < R and arr[row + 1][col] == ".":   # 하
                arr[row + 1][col] = "*"
                water.append([row + 1, col])
            if col - 1 >= 0 and arr[row][col - 1] == ".":  # 좌
                arr[row][col - 1] = "*"
                water.append([row, col - 1])
            if col + 1 < C and arr[row][col + 1] == ".":   # 우
                arr[row][col + 1] = "*"
                water.append([row, col + 1])

        # 위치 업데이트
        length = len(position)
        if length == 0:
            return "KAKTUS"
        for i in range(length):
            row, col = position.popleft()
            if row - 1 >= 0 and arr[row - 1][col] == ".":  # 상
                arr[row - 1][col] = "S"
                position.append([row - 1, col])
            elif row - 1 >= 0 and arr[row - 1][col] == "D":
                return cnt
            if row + 1 < R and arr[row + 1][col] == ".":  # 하
                arr[row + 1][col] = "S"
                position.append([row + 1, col])
            elif row + 1 < R and arr[row + 1][col] == "D":
                return cnt
            if col - 1 >= 0 and arr[row][col - 1] == ".":  # 좌
                arr[row][col - 1] = "S"
                position.append([row, col - 1])
            elif col - 1 >= 0 and arr[row][col - 1] == "D":
                return cnt
            if col + 1 < C and arr[row][col + 1] == ".":  # 우
                arr[row][col + 1] = "S"
                position.append([row, col + 1])
            elif col + 1 < C and arr[row][col + 1] == "D":
                return cnt

        cnt += 1


if __name__ == "__main__":

    # input
    R, C = map(int, sys.stdin.readline().split())
    arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]

    # print
    print(bfs())