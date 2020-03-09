if __name__ == "__main__":
    
    T = int(input())
    
    for i in range(T):
        data_list = list(map(int, input().split()))
        
        for i in range(2):
            max_value = max(data_list)
            data_list.remove(max_value)
        
        print(max(data_list))