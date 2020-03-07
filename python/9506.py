import sys

def factor(n):
    result = []
    
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            result.append(i)
        else:
            continue
    
    return result
    
    
if __name__ == "__main__":
    
    while True:
        N = int(input())
        
        if N == -1:
            break
        else:
            result = factor(N)
            
            if sum(result) == N:
                print("{0} =".format(N), end=" ")
                print(" + ".join(map(str, result)))
            else:
                print("{0} is NOT perfect.".format(N))
            