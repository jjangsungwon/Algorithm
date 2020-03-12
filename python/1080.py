
def change(i, j):
    if i + 2 < N and j + 2 < M:
        for y in range(3):
            for x in range(3):
                A[i + y][j + x] = str(1 - int(A[i + y][j + x]))

if __name__ == "__main__":
    
    N, M = map(int, input().split())
    A = []
    B = []
    
    for t in range(2):
        for i in range(N):
            temp = list(input())
            if t == 0:
                A.append(temp)
            else:
                B.append(temp)
                
    cnt = 0
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                change(i,j)
                cnt += 1
    
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                print(-1)
                exit()
                
    print(cnt)
  