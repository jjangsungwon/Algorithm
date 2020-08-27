if __name__ == "__main__":
    
    for i in range(3):
        
        data_list = list(map(int, input().split()))
        
        front_count, back_count = 0, 0
        
        for i in data_list:
            if i == 0:
                front_count += 1
            elif i == 1:
                back_count += 1
                
        if front_count == 1:
            print("A")
        elif front_count == 2:
            print("B")
        elif front_count == 3:
            print("C")
        elif front_count == 4:
            print("D")
        else:
            print("E")
            