from collections import deque


def topological(goal):
    total_time = [0] * (n + 1)
    q = deque()
    for i in range(1, n + 1):  # 진입차수가 0인 것 삽입
        if indegree[i] == 0:
            q.append(i)

    while q:
        index = q.popleft()
        if index == goal:
            return time[index] + total_time[index]
        for i in range(1, n + 1):
            if graph[index][i]:  # 길이 있다면
                graph[index][i] = False
                indegree[i] -= 1
                total_time[i] = max(total_time[i], total_time[index] + time[index])
                if indegree[i] == 0:
                    q.append(i)


if __name__ == "__main__":
    t = int(input())  # 테스트 케이스의 개수 입력
    for _ in range(t):
        n, k = map(int, input().split())  # 건물의 개수, 규칙의 개수 입력
        time = [0] + list(map(int, input().split()))  # 시간 입력
        graph = [[False] * (n + 1) for _ in range(n + 1)]
        indegree = [0] * (n + 1)

        for _ in range(k):  # 규칙 입력
            a, b = map(int, input().split())
            indegree[b] += 1  # 진입차수 증가
            graph[a][b] = True
        goal = int(input())

        # 출력
        answer = topological(goal)
        print(answer)
