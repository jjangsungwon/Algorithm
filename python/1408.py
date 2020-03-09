
if __name__ == "__main__":
    
    pre = list(map(int, input().split(":")))
    start = list(map(int, input().split(":")))
    
    pre_total = pre[0] * 3600 + pre[1] * 60 + pre[2]
    start_total = start[0] * 3600 + start[1] * 60 + start[2]
    
    value = start_total - pre_total
    
    h = value // 3600
    h %= 24
    value %= 3600
    
    m = value //60
    m %= 60
    value %= 60
    
    s = value //1
    
    # 길이 검사 후 0포함
    time = []
    time.append(h)
    time.append(m)
    time.append(s)

    if time[0] < 10:
        time[0] = "0" + str(time[0])
    if time[1] < 10:
        time[1] = "0" + str(time[1])
    if time[2] < 10:
        time[2] = "0" + str(time[2])
        
    print(":".join(map(str, time)))
    