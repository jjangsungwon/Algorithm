import sys

if __name__ == "__main__":
    
    T = int(input())
    
    for i in range(T):
        N = int(input())
        
        grade = [0 for _ in range(N)]
        result = [0 for _ in range(N)]
        
        for j in range(N):
            grade[j], result[j] = map(float, input().split())
        
        total = 0
        for k in range(N):
            total += grade[k] * result[k]
            
        total /= sum(grade)
        print(int(sum(grade)), total)
        