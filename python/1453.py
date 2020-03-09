
if __name__ == "__main__":
    
    N = int(input())
    people = list(map(int, input().split()))
    visited = [0 for _ in range(101)]
    
    cnt = 0
    for i in people:
        if visited[i] == 0:
            visited[i] = 1
        else:
            cnt += 1
            
    print(cnt)
    