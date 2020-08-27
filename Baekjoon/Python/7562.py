# boj 7562
# blog : jjangsungwon.tistory.com

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


def bfs(c_row, c_col, o_row, o_col):
    arr = [[0] * L for _ in range(L)]

    q = deque([[c_row, c_col]])
    while q:
        row, col = q.popleft()

        if row == o_row and col == o_col:
            return arr[row][col]

        if row - 2 >= 0 and col + 1 < L and arr[row - 2][col + 1] == 0:
            arr[row - 2][col + 1] = arr[row][col] + 1
            q.append([row - 2, col + 1])

        if row - 1 >= 0 and col + 2 < L and arr[row - 1][col + 2] == 0:
            arr[row - 1][col + 2] = arr[row][col] + 1
            q.append([row - 1, col + 2])

        if row + 1 < L and col + 2 < L and arr[row + 1][col + 2] == 0:
            arr[row + 1][col + 2] = arr[row][col] + 1
            q.append([row + 1, col + 2])

        if row + 2 < L and col + 1 < L and arr[row + 2][col + 1] == 0:
            arr[row + 2][col + 1] = arr[row][col] + 1
            q.append([row + 2, col + 1])

        if row + 2 < L and col - 1 >= 0 and arr[row + 2][col - 1] == 0:
            arr[row + 2][col - 1] = arr[row][col] + 1
            q.append([row + 2, col - 1])

        if row + 1 < L and col - 2 >= 0 and arr[row + 1][col - 2] == 0:
            arr[row + 1][col - 2] = arr[row][col] + 1
            q.append([row + 1, col - 2])

        if row - 1 >= 0 and col - 2 >= 0 and arr[row - 1][col - 2] == 0:
            arr[row - 1][col - 2] = arr[row][col] + 1
            q.append([row - 1, col - 2])

        if row - 2 >= 0 and col - 1 >= 0 and arr[row - 2][col - 1] == 0:
            arr[row - 2][col - 1] = arr[row][col] + 1
            q.append([row - 2, col - 1])


if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        L = int(sys.stdin.readline())
        c_row, c_col = map(int, sys.stdin.readline().split())  # 현재 위치
        o_row, o_col = map(int, sys.stdin.readline().split())  # 목표 위치

        print(bfs(c_row, c_col, o_row, o_col))
