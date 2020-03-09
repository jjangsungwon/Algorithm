import sys

if __name__ == "__main__":
    
    data_list = list(map(int, input().split()))
    data_list.sort()
    
    print(" ".join(map(str, data_list)))