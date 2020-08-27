import sys

check =['a', 'e', 'i', 'o', 'u']

if __name__ == "__main__":
    str_list = input()
    cnt = 0
    
    for i in range(len(str_list)):
        if str_list[i] in check:
            cnt += 1
    
    print(cnt)
            
            