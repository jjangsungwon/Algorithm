import sys

if __name__ == "__main__":
    
    X = {}
    y_value = []
    y_index = []
    
    max_index = 0
    
    # X 입력
    N = int(sys.stdin.readline())
    for i in range(N):
        index, value = map(int, sys.stdin.readline().split())
        X[index] = value
            
    # Y 입력
    M = int(sys.stdin.readline())
    for i in range(M):
        index, value = map(int, sys.stdin.readline().split())
        y_index.append(index)
        y_value.append(value)
        
    # a와 b 입력
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    
    # 합계 계산
    total = 0
    
    # a, b
    for j in X.keys():
        
        a_index, b_index = 0, 0
        while a_index < M and y_index[a_index]< j + a:
            a_index += 1
        
        while b_index < M and y_index[b_index]<= j + b:
            b_index += 1
        
        total += X[j] * sum(y_value[a_index:b_index])
        
    print(total)
            
            
            
            
            
            