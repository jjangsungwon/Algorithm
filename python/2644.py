import sys
from collections import defaultdict, deque


def bfs(p1, p2):
    q = deque([p1])
    visited = {p1}

    step = 0
    while q:
        size = len(q)

        for i in range(size):
            index = q.popleft()
            if index == p2:
                return step

            for j in d[index]:
                if j not in visited:
                    visited.add(j)
                    q.append(j)
        step += 1
    return -1


if __name__ == "__main__":

    N = int(input())
    p1, p2 = map(int, sys.stdin.readline().split())
    m = int(input())

    d = defaultdict(set)
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        d[x].add(y)
        d[y].add(x)

    print(bfs(p1, p2))
