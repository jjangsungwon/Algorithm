if __name__ == "__main__":
    
    n = int(input())
    graph = []
    
    for i in range(n):
        temp = list(map(int, input().split()))
        graph.append(temp)
        
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
                    
    for i in range(n):
        print(" ".join(map(str, graph[i])))
    