def dfs(x, y, idx, sum):
    global min
    if idx == N + (N - 1):
        if min > sum:
            min = sum
            return

    # 아래쪽
    if y + 1 < N:
        dfs(x, y + 1, idx + 1, sum + arr[x][y + 1])

    # 오른쪽
    if x + 1 < N:
        dfs(x + 1, y, idx + 1, sum + arr[x + 1][y])


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        arr = []
        min = 10000000
        sum = 0
        for i in range(N):
            temp = list(map(int, input().split()))
            arr.append(temp)

        # 모든 경우 탐색
        dfs(0, 0, 1, arr[0][0])

        print("#{0} {1}".format(tc, min))