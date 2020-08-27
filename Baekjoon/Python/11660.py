if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_list = [list(map(int, input().split())) for _ in range(M)]  # 합을 구해야하는 정보 저장

    # dp 구조 구현
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = arr[0][0]
    for i in range(1, N):
        dp[0][i] = dp[0][i - 1] + arr[0][i]  # 0행 가로
        dp[i][0] = dp[i - 1][0] + arr[i][0]  # 0열 세로
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + arr[i][j] - dp[i - 1][j - 1]

    # 합 계산
    for i in range(M):
        x1, y1, x2, y2 = sum_list[i]
        answer = dp[x2 - 1][y2 - 1]
        if x1 != 1:
            answer -= dp[x1 - 2][y2 - 1]
        if y1 != 1:
            answer -= dp[x2 - 1][y1 - 2]
        if y1 != 1 and x1 != 1:
            answer += dp[x1 - 2][y1 - 2]
        print(answer)
