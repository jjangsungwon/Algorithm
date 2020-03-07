import sys

if __name__ == "__main__":
    T = int(input())
    
    for i in range(T):
        str_list = list(map(str, sys.stdin.readline().strip().split()))
        
        for j in range(len(str_list)):
            for k in range(len(str_list[j]) -1 , -1, -1):
                print(str_list[j][k], end="")
            
            if j != len(str_list) -1:
                print(" ", end="")
        print("")