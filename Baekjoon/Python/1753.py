import sys
from heapq import heappush, heappop

if __name__ == "__main__":
    V, E = map(int, input().split())
    K = int(input())  # 시작 정점

    arr = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        arr[u].append([v, w])

    distance = [sys.maxsize] * (V + 1)
    visited = [False] * (V + 1)
    distance[K] = 0

    q = []
    heappush(q, [0, K])

    while q:
        cost, pos = heappop(q)

        for p, c in arr[pos]:
            c += cost
            if c < distance[p]:
                distance[p] = c
                heappush(q, [c, p])

    # print
    for i in range(1, V + 1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print("INF")
