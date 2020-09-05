INF = 1e9


if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [[INF] * (v + 1) for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a][b] = c

    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    min_distance = INF
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            min_distance = min(min_distance, graph[i][j] + graph[j][i])
    if min_distance == INF:
        print(-1)
    else:
        print(min_distance)

