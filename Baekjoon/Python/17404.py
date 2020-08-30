import copy

INF = 1e9
if __name__ == "__main__":
    n = int(input())  # 집의 수 입력받기
    cost = [list(map(int, input().split())) for _ in range(n)]  # 페인트 비용 값 입력받기
    dp = [[INF] * n for _ in range(n)]

    # dp 배열 첫 행은 array 첫 행 값 대입
    for i in range(3):
        dp[0][i] = cost[0][i]

    # dp 탐색
    answer = INF
    for start in range(3):  # start를 시작점으로
        dp[0][0], dp[0][1], dp[0][2] = INF, INF, INF  # 다른 지점은 시작 못하도록 무한대로 초기화
        dp[0][start] = 0
        for i in range(1, n):
            dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])  # R
            dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])  # G
            dp[i][2] = cost[i][2] + min(dp[i  -1][0], dp[i - 1][1])  # B
        if start == 0:
            answer = min(answer, cost[0][start] + dp[n - 1][1], cost[0][start] + dp[n - 1][2])
        elif start == 1:
            answer = min(answer, cost[0][start] + dp[n - 1][0], cost[0][start] + dp[n - 1][2])
        else:
            answer = min(answer, cost[0][start] + dp[n - 1][0], cost[0][start] + dp[n - 1][1])

    # 출력
    print(answer)