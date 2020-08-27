from collections import deque


def bfs(val):
    q = deque()
    q.append(start)
    visited = {start}

    while q:
        y = q.popleft()
        for x, w in data[y]:
            if x not in visited and w >= val:
                visited.add(x)
                q.append(x)
    if end in visited:
        return True
    else:
        return False


if __name__ == "__main__":
    N, M = map(int, input().split())
    data = [[] for _ in range(N + 1)]  # 연결 정보
    for _ in range(M):
        start, end, weight = map(int, input().split())
        data[start].append((end, weight))
        data[end].append((start, weight))
    start, end = map(int, input().split())

    left, right = 1, 1000000000

    answer = 1
    while left <= right:
        mid = (left + right) // 2
        if bfs(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    print(answer)
