import sys

if __name__ == "__main__":
    N = int(input())
    
    student = [0 for _ in range(N)]
    apple = [0 for _ in range(N)]
    
    for i in range(N):
        student[i], apple[i] = map(int, input().split())
        
    total = 0
    
    for i in range(N):
        total += apple[i] % student[i]
    
    print(total)