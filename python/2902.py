import sys

if __name__ == "__main__":
    
    data_list = list(input().split("-"))
    result = []
    
    for i in range(len(data_list)):
        result.append(data_list[i][0])
        
    print("".join(result))
    