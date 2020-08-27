# boj 10451
# blog : jjangsungwon.tistory.com
import sys


def dfs(row):
    for i in range(1, N + 1):
        if arr[row][i] == 1:
            arr[row][i] = 0
            arr[i][row] = 0
            dfs(i)


if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        N = int(input())
        num = list(map(int, sys.stdin.readline().split()))
        num.insert(0, 0)  # 인덱스 편리성을 위해서 추가

        # 연결 그래프
        arr = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(1, len(num)):
            arr[i][num[i]] = 1
            arr[num[i]][i] = 1

        count = 0
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if arr[i][j] == 1:
                    count += 1
                    dfs(i)
        print(count)
