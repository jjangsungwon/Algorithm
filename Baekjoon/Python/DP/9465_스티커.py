import sys


if __name__ == "__main__":

    t = int(sys.stdin.readline())  # 테스트 케이스 개수
    for _ in range(t):
        # 스티커 값 입력 받기
        n = int(sys.stdin.readline())  # 정수 개수(열의 수)
        array = []
        for _ in range(2):
            array.append(list(map(int, sys.stdin.readline().split())))

        if n == 1:
            print(max(array[0][0], array[1][0]))
        else:
            # 다이나믹 프로그래밍
            # dp[i][j] : array[i][j] 스티커를 골랐을 때 최대 점수(j열까지 진행한 경우)
            dp = [[0] * n for _ in range(2)]
            for i in range(2):
                dp[i][0], dp[i][1] = array[i][0], array[i][1]
            dp[0][1] += dp[1][0]
            dp[1][1] += dp[0][0]

            for j in range(2, n):
                dp[0][j] = array[0][j] + max(dp[1][j - 1], dp[1][j - 2])
                dp[1][j] = array[1][j] + max(dp[0][j - 1], dp[0][j - 2])

            print(max(max(dp[0]), max(dp[1])))

