
if __name__ == "__main__":
    
    n = int(input())
    data_list = list(map(int, input().split()))
    line = []
    
    for i in range(len(data_list)-1, -1, -1):
        line.insert(data_list[i], i +1)
    
    
    print(" ".join(map(str, line)))