from operator import itemgetter
import sys

if __name__ == "__main__":
    
    T = int(sys.stdin.readline())
    
    for i in range(T):
        N = int(sys.stdin.readline())
        
        data = []
        min_value = [0 for _ in range(N)]
        
        for j in range(N):
            temp = list(map(int, sys.stdin.readline().split()))
            data.append(temp)
            
        cnt = 1
        data.sort(key = itemgetter(0, 1))
        min_value[0] = data[0][1]
        
        for j in range(1, N):
            min_value[j] = data[j][1]
        
            if min_value[j] > min_value[j-1]:
                min_value[j] = min_value[j-1]
        
        
        for i in range(1, N):
            if data[i][1] < min_value[i-1]:
                cnt += 1
        
        print(cnt)