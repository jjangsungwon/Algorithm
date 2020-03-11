def dfs(y, x):
    global cnt
    cnt += 1
    visited[y][x] = 1 # 방문 여부 표시
    
    # 위
    if y -1 >= 0:
        if map[y-1][x] == "1" and visited[y-1][x] == 0:
            dfs(y-1, x)
        
    # 아래
    if y + 1 < n:
        if map[y + 1][x] == "1" and visited[y+1][x] == 0:
            dfs(y + 1, x)

    # 좌
    if x - 1 >= 0:
        if map[y][x - 1] == "1" and visited[y][x-1] == 0:
            dfs(y, x - 1)
    
    # 우
    if x + 1 < n:
        if map[y][x + 1] == "1" and visited[y][x+1] == 0:
            dfs(y, x + 1)
    
    return
    
if __name__ == "__main__":
    
    n = int(input())
    visited = [[0] * n for _ in range(n)]
    numlist = []
    map = []
    cnt = 0
    
    # 지도 입력
    for i in range(n):dk
        temp = list(input())
        map.append(temp)
    
    for i in range(n):
        for j in range(n):
            if map[i][j] == "1" and visited[i][j] == 0:
                dfs(i, j)             
                numlist.append(cnt)
                cnt = 0
                
    numlist.sort()
    print(len(numlist))
    for i in range(len(numlist)):
        print(numlist[i])