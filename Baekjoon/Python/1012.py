# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j):
    global n
    visited[i][j] = 1
    
    q = []
    q.append((i,j))
    
    while q:
        current = q.pop(0)
        
        for k in range(4):
            y = current[0] + dy[k]
            x = current[1] + dx[k]
            if 0<=y<row and 0<=x<col:
                if visited[y][x] == 0 and arr[y][x] == 1:
                    q.append((y,x))
                    visited[y][x] = 1

if __name__ == "__main__":
    
    T = int(input())
    
    for k in range(T):
        cnt = 0
        row, col, num = map(int, input().split())
        arr = [[False] * col for _ in range(row)]
        visited = [[False] * col for _ in range(row)]
            
        for i in range(num):
            y, x = map(int, input().split())
            arr[y][x] = True    

        for i in range(row):
            for j in range(col):
                if arr[i][j] == 1 and visited[i][j] == 0:
                    bfs(i, j)
                    cnt += 1

        print(cnt)

                