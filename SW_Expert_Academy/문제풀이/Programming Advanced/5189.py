def dfs(count, idx, sum, visited):
    global min

    if count == N:
        sum += arr[idx][0]
        if min > sum:
            min = sum

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(count + 1, i, sum + arr[idx][i], visited)
            visited[i] = 0


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        arr = []
        visited = [0 for _ in range(N)]
        min = 10000000
        sum = 0

        for i in range(N):
            temp = list(map(int, input().split()))
            arr.append(temp)

        visited[0] = 1
        dfs(1, 0, sum, visited)

        print("#{0} {1}".format(tc, min))
