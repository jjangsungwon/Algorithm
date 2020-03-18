import sys


def binary(idx, VKeys, VVals):
    def getRecursive(lookfor, start, end):
        mid = (start + end) // 2
        if VKeys[mid] <= lookfor < VKeys[mid + 1]:
            return mid
        if lookfor < VKeys[mid]:
            return getRecursive(lookfor, start, mid)
        if VKeys[mid + 1] <= lookfor:
            return getRecursive(lookfor, mid + 1, end)

    if idx < VKeys[0]:
        return 0
    if VKeys[-1] <= idx:
        return VVals[-1]
    return VVals[getRecursive(idx, 0, len(VKeys) - 1)]


if __name__ == "__main__":

    # X 입력
    N = int(sys.stdin.readline())
    x_index = [None] * N
    x_value = [None] * N

    for i in range(N):
        index, value = map(int, sys.stdin.readline().split())
        x_index[i], x_value[i] = index, value

    # Y 입력
    M = int(sys.stdin.readline())
    y_index = [None] * M
    y_value = [None] * M
    for i in range(M):
        index, value = map(int, sys.stdin.readline().split())
        y_index[i], y_value[i] = index, value

    # a와 b 입력
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())

    # 합계 계산
    indexs = [None] * M
    vals = [None] * M

    indexs[0], vals[0] = y_index[0], y_value[0]

    for i in range(1, M):
        indexs[i], vals[i] = y_index[i], y_value[i] + vals[i - 1]

    total = 0
    for i in range(N):
        keyval = x_index[i]
        total += x_value[i] * (binary(keyval + b, indexs, vals) - binary(keyval + a - 1, indexs, vals))

    print(total)
