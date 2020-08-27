def dfs(data, visited, count, val):
    global total
    
    if count == N:
        if val < total:
            total = val
    
    if val > total:
        return
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(data, visited, count + 1, val + data[count][i])
            visited[i] = 0    

if __name__ == "__main__":
    
    T = int(input())
    
    for tc in range(1, T + 1):
        N = int(input())
        data = []
        visited = [0 for _ in range(N)]
        total = 10000
        for i in range(N):
            temp = list(map(int, input().split()))
            data.append(temp)
        
        dfs(data, visited, 0, 0)
            
        print("#{} {}".format(tc, total))