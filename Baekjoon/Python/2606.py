def dfs(row, N, visited):
    global cnt
    for i in range(N):
        if arr[row][i] == 1 and i not in visited:
            visited.append(i)
            dfs(i, N, visited)


if __name__ == "__main__":

    N = int(input())
    M = int(input())

    arr = [[0] * N for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        arr[A - 1][B - 1] = 1
        arr[B - 1][A - 1] = 1

    visited = []
    cnt = 0
    dfs(0, N, visited)
    if len(visited) == 0:
        print(0)
    else:
        print(len(set(visited)) - 1)