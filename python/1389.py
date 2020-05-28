import sys


def dfs(start, goal, visited, move):
    global val

    if start == goal:
        val = min(val, move)
        return

    for i in range(N):
        if people[start][i] != 0 and i not in visited:
            visited.append(i)
            dfs(i, goal, visited, move + 1)
            visited.pop()


if __name__ == "__main__":

    N, M = map(int, input().split())
    people = [[0] * N for _ in range(N)]

    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        people[A - 1][B - 1], people[B - 1][A - 1] = 1, 1

    min_people, min_value = -1, sys.maxsize

    # 0번 사람부터 실행
    for i in range(N):
        total, val = 0, 0
        for j in range(N):
            val = sys.maxsize
            if i == j:
                continue
            else:
                dfs(i, j, [i], 0) # i에서 j까지
                total += val
        if min_value > total:
            min_value = total
            min_people = i

    print(min_people + 1)
