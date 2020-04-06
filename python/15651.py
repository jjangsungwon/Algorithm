import itertools

# 내장 함수 사용
'''
if __name__ == "__main__":

    N, M = map(int, input().split())
    temp = [i for i in range(1, N + 1)]
    data = itertools.product(temp, repeat = M)

    for i in data:
        print(" ".join(map(str, i)))
'''


def backtracking(arr, k):
    if k == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, N + 1):
        arr[k] = i
        backtracking(arr, k + 1)


# 백트래킹 활용
if __name__ == "__main__":
    N, M = map(int, input().split())

    arr = [0 for _ in range(M)]
    k = 0

    backtracking(arr, 0)
