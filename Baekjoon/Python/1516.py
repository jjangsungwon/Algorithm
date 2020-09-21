import copy
from collections import deque


def topological():
    q = deque()
    finish = [False] * (n + 1)
    pre_time = copy.deepcopy(t)
    post_time = [0] * (n + 1)
    result_time = [0] * (n + 1)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            finish[i] = True
            result_time[i] = t[i]  # 바로 건물을 지을 수 있다.

    copy_q = deque()
    while True:
        while q:
            index = q.popleft()
            for i in range(1, n + 1):
                if graph[index][i]:
                    indegree[i] -= 1
                    if post_time[i] < pre_time[i] + result_time[index]:
                        post_time[i] = pre_time[i] + result_time[index]
                    if indegree[i] == 0:
                        finish[i] = True
                        result_time[i] = post_time[i]
                        copy_q.append(i)

        if len(copy_q) == 0:
            break
        else:
            q.extend(copy_q)
            copy_q = deque()

    return result_time


if __name__ == "__main__":
    n = int(input())  # 건물의 종류 수
    graph = [[False] * (n + 1) for _ in range(n + 1)]  # 건물 순서 그래프
    indegree = [0] * (n + 1)  # 각 건물을 짓기 위해서 먼저 지어야 하는 건물의 수
    t = [0] * (n + 1)  # 각 건물을 짓는데 걸리는 시간

    for i in range(1, n + 1):
        data = list(map(int, input().split()))
        t[i] = data[0]
        for j in range(1, len(data) - 1):
            graph[data[j]][i] = True
            indegree[i] += 1

    result = topological()
    for i in range(1, n + 1):
        print(result[i])
