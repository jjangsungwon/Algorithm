def backtracking(idx, count, data):
    global cnt
    
    if idx + data[idx] >= data[0]:
        if count < cnt:
            cnt = count
        return
    
    if count > cnt:
        return
    
    start_battery = data[idx]
    for i in range(1, start_battery + 1):
        backtracking(idx + i, count + 1, data)

if __name__ == "__main__":
    
    T = int(input())
    
    for tc in range(1, T + 1):
        cnt = 100000
        data_list = list(map(int, input().split()))
        
        backtracking(1, 0, data_list)
        
        print("#{} {}".format(tc, cnt))