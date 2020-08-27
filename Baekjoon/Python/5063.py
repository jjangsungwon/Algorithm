import sys

if __name__ == "__main__":
    
    T = int(input())
    
    for tc in range(1, T + 1):
        data_list = list(map(int, input().split()))
        
        if data_list[0] < data_list[1] - data_list[2]:
            print("advertise")
        elif data_list[0] > data_list[1] - data_list[2]:
            print("do not advertise")
        else:
            print("does not matter")