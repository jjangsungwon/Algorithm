def dfs(start, end):
    global result
    visited[start] = 1
    for next in range(1, v + 1):
        if MyMap[start][next] != 0:
            if next == end:
                result = 1
            dfs(next, end)


TC = int(input())
result = 0

for tc in range(1, TC + 1):
    v, e = map(int, input().split())
    MyMap = [[0] * (v + 1) for _ in range(v + 1)]
    visited = [0] * (v + 1)
    result = 0
    for j in range(1, e + 1):
        temp_v, temp_e = map(int, input().split())
        MyMap[temp_v][temp_e] = 1

    start, end = map(int, input().split())
    dfs(start, end)

    if result == 1:
        print('#{0} 1'.format(tc))
    else:
        print('#{0} 0'.format(tc))