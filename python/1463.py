import sys
import math
    
    
if __name__ == "__main__":
    
    N = int(input())
    d = [0 for _ in range(N+1)]
    
    for i in range(N + 1):
        if i <= 1:
            continue
        else:
            d[i] = d[i-1]
            
            if i % 3 == 0:
                if d[i//3] < d[i]:
                    d[i] = d[i//3]
            
            if i % 2 == 0:
                if d[i//2] < d[i]:
                    d[i] = d[i//2]
            
            d[i] += 1
                
            
    print(d[N])
    
    
    
    