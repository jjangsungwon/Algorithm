import sys

if __name__ == "__main__":
    
    T = int(input())
    
    for tc in range(1, T + 1):
        P, M = map(int, input().split())
        arr = [0 for _ in range(M + 1)]
        
        for i in range(P):
            check = int(input())
            arr[check] += 1
        
        for i in range(1, M + 1):
            if arr[i] >= 1:
                arr[i] -= 1
        
        print(sum(arr))
        
        