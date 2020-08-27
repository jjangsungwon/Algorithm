import sys


def backtracking(arr, isused, k):
    if k == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, N+1):
        if isused[i] == 0:
            arr[k] = i
            isused[i] = 1
            backtracking(arr, isused, k + 1)
            isused[i] = 0


if __name__ == "__main__":
    # input
    N, M = map(int, sys.stdin.readline().split())

    # declare and assign variables
    isused = [0 for _ in range(N+1)]
    arr = [0 for _ in range(M)]
    k = 0

    # call backtracking
    backtracking(arr, isused, 0)



