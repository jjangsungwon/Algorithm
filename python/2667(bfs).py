# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j):
    global cnt, n
    visited[i][j] = 1
    cnt += 1
    
    q = []
    q.append((i,j))
    
    while q:
        current = q.pop(0)
        
        for k in range(4):
            y = current[0] + dy[k]
            x = current[1] + dx[k]
            if 0<=y<n and 0<=x<n:
                if visited[y][x] == 0 and map[y][x] == "1":
                    q.append((y,x))
                    visited[y][x] = 1
                    cnt += 1

if __name__ == "__main__":
    
    n = int(input())
    map = []
    num_list = []
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    
    for i in range(n):
        temp = list(input())
        map.append(temp)
        
    for i in range(n):
        for j in range(n):
            if map[i][j] == "1" and visited[i][j] == 0:
                bfs(i, j)
                num_list.append(cnt)
                cnt = 0
    
    print(len(num_list))
    
    for i in range(len(num_list)):
        print(num_list[i])
        
                