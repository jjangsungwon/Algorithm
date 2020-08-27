
if __name__ == "__main__":
    
    string = input()
    
    
    check, cnt, flag = 0, 0, 1
    pre_value = string[0]
    
    for i in range(1, len(string)):
        if string[i] != pre_value:
            if string[i] != string[0]:
                cnt += 1
            pre_value = string[i]
    
    print(cnt)