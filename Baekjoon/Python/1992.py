# boj 1992
# blog : jjangsungwon.tistory.com
import sys

result = ""


def divide(N, row, col):
    global result
    val = 0
    for i in range(row, row + N):
        for j in range(col, col + N):
            val += arr[i][j]

    if val == 0:
        result += "0"
    elif val == N * N:
        result += "1"
    else:
        result += "("
        divide(N // 2, row, col)  # 왼쪽 위
        divide(N // 2, row, col + N // 2)  # 오른쪽 위
        divide(N // 2, row + N // 2, col)  # 왼쪽 아래
        divide(N // 2, row + N // 2, col + N // 2)  # 오른쪽 아래
        result += ")"


if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

    divide(N, 0, 0)
    print(result)
