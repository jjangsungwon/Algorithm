import sys
from collections import deque

if __name__ == "__main__":

    # input
    N, M = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

    # search
    answer = 0
    for i in range(N):
        for j in range(M):
            if i > 0 and j > 0 and arr[i][j] == 1:
                arr[i][j] += min(arr[i - 1][j - 1], arr[i - 1][j], arr[i][j - 1])
            answer = max(answer, arr[i][j])
    # for i in range(N):
    #     print(arr[i])
    print(answer * answer)
