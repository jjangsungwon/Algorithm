import sys
import copy
from collections import deque
sys.setrecursionlimit(10 ** 9)


def bfs(start, end):
    q = deque()
    # 초기에 움직일 수 있는 위치 추가
    for i in range(len(e)):
        if (start - e[i][0]) % e[i][1] == 0:
            q.append(([i + 1], 1))
            if end >= e[i][0] and (end - e[i][0]) % e[i][1] == 0:
                return [i + 1], 1
    else:
        while q:
            use, cnt = q.popleft()
            for i in range(len(e)):
                if (i + 1) not in use:
                    for index in range(e[i][0], n + 1, e[i][1]):
                        if (index >= e[use[-1] - 1][0]) and (index - e[use[-1] - 1][0]) % e[use[-1] - 1][1] == 0:
                            new_use = copy.deepcopy(use)
                            new_use.append(i + 1)
                            q.append((new_use, cnt + 1))
                            if (end >= e[i][0]) and (end - e[i][0]) % e[i][1] == 0:
                                return new_use, cnt + 1
                            break
        return [], -1


if __name__ == "__main__":

    n, m = map(int, sys.stdin.readline().split())
    e = []
    min_floor = 1e9
    for _ in range(m):  # 엘리베이터
        a, b = map(int, sys.stdin.readline().split())
        min_floor = min(min_floor, a)
        e.append((a, b))
    a, b = map(int, sys.stdin.readline().split())

    if b < min_floor:
        print(-1)
    else:
        use_list, answer = bfs(a, b)
        if answer != -1:
            print(answer)
            for i in range(len(use_list)):
                print(use_list[i])
        else:
            print(-1)
