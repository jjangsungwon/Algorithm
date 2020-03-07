import sys
from operator import itemgetter

if __name__ == "__main__":
    
    N = int(input())
    data = []
    
    for i in range(N):
        temp = list(map(str, input().split()))
        
        temp[1] = int(temp[1])
        temp[2] = int(temp[2])
        temp[3] = int(temp[3])
        
        data.append(temp)
    
    data.sort(key=itemgetter(3,2,1))
  
    print(data[N-1][0])
    print(data[0][0])  
        
    
        