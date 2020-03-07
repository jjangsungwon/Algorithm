import sys

if __name__ == "__main__":
    T = int(input())
    
    for tc in range(1, T + 1):
        num_list = list(map(int, input().split()))
        num_list.pop(0)
        num_list.sort(reverse=True)
        
        max_value = num_list[0]
        min_value = num_list[-1]
        
        gap = -1
        for i in range(len(num_list) - 1):
            if num_list[i] - num_list[i+1] > gap:
                gap = num_list[i] - num_list[i+1]
        
        print("Class {0}".format(tc))
        print("Max {0}, Min {1}, Largest gap {2}".format(max_value, min_value, gap))
        
        
        