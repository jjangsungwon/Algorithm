import sys
import time

if __name__ =="__main__":
    str_list = list(map(str, input()))
    result = []
    
    idx = 0
    while idx < len(str_list):
        if str_list[idx] == '<':
            while str_list[idx] != '>':
                result.append(str_list[idx])
                idx += 1
            result.append('>')
            idx += 1
        else:
            temp = []
            while idx < len(str_list) and str_list[idx] != ' ' and str_list[idx] != '<':
                temp.append(str_list[idx])
                idx += 1
            
            if idx == len(str_list) - 1:
                temp.reverse()
            else:
                temp.reverse()
                if idx < len(str_list) and str_list[idx] == '<':
                    pass
                else:
                    temp.append(' ')
                    idx += 1
            result.append("".join(map(str, temp)))
    
    print("".join(map(str, result)))