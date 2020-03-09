
if __name__ == "__main__":
    
    for i in range(3):
        num = input()
        
        pre_val = int(num[0])
        
        max_length = 1
        cnt = 1
        for i in range(1, len(num)):
            if pre_val == int(num[i]):
                cnt += 1
                pre_val = int(num[i])
            else:
                if max_length < cnt:
                    max_length = cnt
                pre_val = int(num[i])
                cnt = 1
        
        if cnt > max_length:
            max_length = cnt
            
        print(max_length)
            