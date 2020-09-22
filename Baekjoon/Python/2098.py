INF = int(1e9)


def tsp(index, before):
    if before == ((1 << n) - 1):  # 모든 경로를 방문한 경우
        if graph[index][0] > 0:  # 다시 돌아갈 수 있는 상황
            return graph[index][0]
        else:  # 다시 돌아갈 수 없는 상황
            return INF

    if dp[index][before] > 0:  # 방문한 적이 있는 경우
        return dp[index][before]

    tmp = INF
    for i in range(1, n):
        if not (before >> i) & 1 and graph[index][i] != 0:
            tmp = min(tmp, graph[index][i] + tsp(i, before | (1 << i)))
    dp[index][before] = tmp
    return tmp


if __name__ == "__main__":
    n = int(input())  # 도시의 수
    graph = [list(map(int, input().split())) for _ in range(n)]

    # dp 배열 초기화
    dp = [[0] * (1 << n) for _ in range(n)]  # (현재 위치, 이전까지 방문한 위치)

    answer = tsp(0, 1)
    print(answer)

