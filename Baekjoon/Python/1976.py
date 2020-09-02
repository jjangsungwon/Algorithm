if __name__ == "__main__":
    n = int(input())  # 총 도시의 수
    m = int(input())  # 여행 계획에 속한 도시들의 수
    graph = [list(map(int, input().split())) for _ in range(n)]
    move = list(map(int, input().split()))

    # 플로이드-워셜 알고리즘을 통해 모든 노드 간의 최소 거리를 구한다.
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0 and i != j:  # 길이 없다는 뜻
                graph[i][j] = 1e9  # 10억으로 대입

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 여행 여부 확인
    flag = True
    pre_index = move[0] - 1
    for i in range(1, m):
        if graph[pre_index][move[i] - 1] >= 1e9:  # 길이 없는 경우
            flag = False
            break
        else:
            pre_index = move[i] - 1

    if flag:
        print("YES")
    else:
        print("NO")