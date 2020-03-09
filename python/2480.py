
if __name__ == "__main__":
    
    data_list = list(map(int, input().split()))
    
    max_count = 0
    index = 0
    
    for i in range(3):
        count = -1
        for j in range(3):
            if data_list[i] == data_list[j]:
                count += 1            
        if max_count < count:
            index = i
            max_count = count
    
    value = 9
    if max_count == 0:
        value = max(data_list) * 100
    elif max_count == 1:
        value = 1000 + (data_list[index]) * 100
    else:
        value = 10000 + (data_list[index]) * 1000
    
    print(value)
    