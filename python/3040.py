import sys

def dfs(idx, count, data):
    
    if count == 7:
        if sum(data) == 100:
            print("\n".join(map(str, data)))
            exit()
        return
    
    if sum(data) > 100:
        return
    
    if idx >= 9:
        return
    
    data.append(data_list[idx])
    dfs(idx + 1, count + 1, data)
    data.pop()
    dfs(idx + 1, count, data)
    

if __name__ == "__main__":
    
    data_list = []
    
    for i in range(9):
        data_list.append(int(input()))
    
    start = []
    dfs(0, 0, start)