import sys

if __name__ == "__main__":
    
    N = int(input())
    k_num = 0
    y_num = 0
    
    for i in range(N):
        
        for j in range(9):
            Y, K = map(int, input().split())
        
            y_num += Y
            k_num += K
            
        if k_num > y_num:
            print("Korea")
        elif k_num == y_num:
            print("Draw")
        else:
            print("Yonsei")
        