import sys

if __name__ == "__main__":
    data_list = sys.stdin.readline().strip()
    
    height = 10
    pre_value = data_list[0]
    
    for i in range(1, len(data_list)):
        if data_list[i] == pre_value:
            height += 5
            pre_value = data_list[i]
        else:
            height += 10
            pre_value = data_list[i]
    
    print(height)
    
    