import sys

def possible(x, y, op):
    if op == "<":
        return x < y
    elif op == ">":
        return x > y

def backtracking(idx, value):
    global max_value, min_value

    if idx == n + 1: 
        if not min_value:
            min_value = value
        else:
            max_value = value
        return
    else:
        for i in range(10):
            if not visited[i]:
                if idx == 0 or possible(int(value[-1]), i, op[idx-1]):
                    visited[i] = True
                    backtracking(idx + 1, value + str(i))
                    visited[i] = False
        
if __name__ == "__main__":
    
    n = int(input())
    op = input().split()
    
    visited = [0 for _ in range(10)]
    
    max_value = ""
    min_value = ""
    
    backtracking(0, "")
    
    print(max_value)
    print(min_value)
    