import sys


def dfs(k):
    global count
    if k == N:
        count += 1
        return

    for i in range(N):
        if not (column[i] or left[k + i] or right[k - i + N - 1]):
            column[i] = left[k + i] = right[k - i + N - 1] = 1
            dfs(k + 1)
            column[i] = left[k + i] = right[k - i + N - 1] = 0


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    column, left, right = [0] * N, [0] * (2 * N - 1), [0] * (2 * N - 1)
    count = 0

    dfs(0)
    print(count)
