import sys

if __name__ == "__main__":
    
    T = int(input())
    
    for tc in range(1, T + 1):
        N = int(input())
        data_list = list(map(int, input().split()))
        
        print((max(data_list) - min(data_list)) * 2)
        