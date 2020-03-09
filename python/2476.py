
if __name__ == "__main__":
    
    T = int(input())
    
    max_value = 0
    for i in range(T):
        data_list = list(map(int, input().split()))

        max_count = 0
        index = 0

        for data in data_list:
            if max_count < data_list.count(data):
                max_count = data_list.count(data)
                index = data_list.index(data)

        value = 0
        if max_count == 1:
            value = max(data_list) * 100
        elif max_count == 2:
            value = 1000 + (data_list[index]) * 100
        else:
            value = 10000 + (data_list[index]) * 1000

        if max_value < value:
            max_value = value
    
    print(max_value)