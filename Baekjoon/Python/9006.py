import sys

if __name__ == "__main__":
    
    T = int(input())
    
    for i in range(T):
        str_list = sys.stdin.readline().strip()
        
        if len(str_list) <= 1:
            result = str_list + str_list
        else:
            result = str_list[0] + str_list[-1]
        
        print(result)