import math

if __name__ == "__main__":
    
    N = int(input())
    
    val = 0
    i = 1
    while True:
        if i * (i+1) <= 2 * N:
            val = i
        else:
            break
            
        i += 1
    
    print(val)