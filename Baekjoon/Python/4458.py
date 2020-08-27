import sys

if __name__ == "__main__":
    
    T = int(input())
    
    for i in range(T):
        line = list(input())
        
        
        if 65 <= ord(line[0]) <= 90:
                    pass
        elif 97<= ord(line[0]) <= 122:
                    line[0] = chr(ord(line[0]) - 32)
        
        print("".join(map(str, line)))
    
     