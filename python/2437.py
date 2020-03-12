
if __name__ == "__main__":
    
    n = int(input())
    data_list = list(map(int, input().split()))
    data_list.sort()

    if data_list[0] != 1:
        print(1)
    else:
        total = 1
        
        for i in range(1, n):
            if data_list[i] > total + 1:
                break
            total += data_list[i]
        
        print(total + 1)