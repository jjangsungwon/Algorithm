def Backtracking(r, c, d):
    global answer

    if r == N - 1 and c == N - 1:
        answer += 1
    else:
        # 가로
        if d == 0 or d == 2:  # 가로 혹은 대각선 방향일때 가로로 이동 가능.
            if c + 1 < N and arr[r][c + 1] == 0:
                Backtracking(r, c + 1, 0)

        # 세로
        if d == 1 or d == 2:  # 세로 혹은 대각선 방향일때 세로로 이동 가능
            if r + 1 < N and arr[r + 1][c] == 0:
                Backtracking(r + 1, c, 1)

        # 대각선
        if r + 1 < N and c + 1 < N:
            if arr[r + 1][c] == arr[r][c + 1] == arr[r + 1][c + 1] == 0:
                Backtracking(r + 1, c + 1, 2)


if __name__ == "__main__":
    # input
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    Backtracking(0, 1, 0)
    print(answer)
