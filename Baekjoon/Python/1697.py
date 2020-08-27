from collections import deque


def bfs(start, end):
    visited = set()
    if start == end:
        return 0
    else:
        q = deque([start])
        cnt = 1
        while True:
            temp = deque()
            while q:
                val = q.popleft()
                if val - 1 == end or val + 1 == end or val * 2 == end:
                    print(cnt)
                    exit()
                else:
                    if val - 1 >= 0 and val - 1 not in visited:
                        visited.add(val - 1)
                        temp.append(val - 1)

                    if val + 1 < 100001 and val + 1 not in visited:
                        visited.add(val + 1)
                        temp.append(val + 1)

                    if val * 2 < 100001 and val * 2 not in visited:
                        visited.add(val * 2)
                        temp.append(val * 2)
            cnt += 1
            q.extend(temp)


if __name__ == "__main__":

    N, K = map(int, input().split())
    if N > K:
        print(N - K)
    else:
        print(bfs(N, K))