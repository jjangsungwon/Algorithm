import sys

if __name__ == "__main__":
    str_list = sys.stdin.readline()
    cnt = 0
    
    for i in range(len(str_list)):
        if str_list[i] == ",":
            cnt += 1
    
    print(cnt + 1)
            