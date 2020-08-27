import sys
from operator import itemgetter

if __name__ == "__main__":
    N = int(input())
    arr = []
    
    for i in range(N):
        temp = []
        x, y = map(int, input().split())
        temp.append(x)
        temp.append(y)
        arr.append(temp)
    
    arr.sort(key=itemgetter(1,0))
    
    for i in range(N):
        print(" ".join(map(str, arr[i])))
        
        
    