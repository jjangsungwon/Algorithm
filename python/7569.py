# boj 7569
# blog : jjangsungwon.tistory.com

import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)


def bfs():
    temp = []
    zero_cnt = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:
                    temp.append([h, i, j])
                elif arr[h][i][j] == 0:
                    zero_cnt += 1

    q = deque(temp)
    cnt = 0

    while zero_cnt:
        temp = []
        while q:
            h, row, col = q.popleft()

            # 상
            if row - 1 >= 0 and arr[h][row - 1][col] == 0:
                arr[h][row - 1][col] = 1
                temp.append([h, row - 1, col])
                zero_cnt -= 1

            # 하
            if row + 1 < N and arr[h][row + 1][col] == 0:
                arr[h][row + 1][col] = 1
                temp.append([h, row + 1, col])
                zero_cnt -= 1

            # 좌
            if col - 1 >= 0 and arr[h][row][col - 1] == 0:
                arr[h][row][col - 1] = 1
                temp.append([h, row, col - 1])
                zero_cnt -= 1

            # 우
            if col + 1 < M and arr[h][row][col + 1] == 0:
                arr[h][row][col + 1] = 1
                temp.append([h, row, col + 1])
                zero_cnt -= 1

            # 높 -> 위
            if h + 1 < H and arr[h + 1][row][col] == 0:
                arr[h + 1][row][col] = 1
                temp.append([h + 1, row, col])
                zero_cnt -= 1

            # 높 -> 낮
            if h - 1 >= 0 and arr[h - 1][row][col] == 0:
                arr[h - 1][row][col] = 1
                temp.append([h - 1, row, col])
                zero_cnt -= 1

        q.extend(temp)
        cnt += 1

        if len(q) == 0 and zero_cnt:
            return -1
    return cnt


if __name__ == "__main__":

    # input
    M, N, H = map(int, input().split())
    arr = []

    for _ in range(H):
        arr.append([list(map(int, sys.stdin.readline().split())) for _ in range(N)])

    print(bfs())
