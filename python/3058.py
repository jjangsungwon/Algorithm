import sys

if __name__ == "__main__":
    
    T = int(input())
    
    for i in range(T):
        min_val = sys.maxsize
        total = 0
        data_list = list(map(int, input().split()))
        
        for data in data_list:
            if data % 2 == 0:
                total += data
                if min_val > data:
                    min_val = data
        
        print(total, min_val)