import time

if __name__ == "__main__":
    
    N = int(input())
    
    result = []
    
    if N == 0:
        print(0)
    else:
        while N:

            if N % -2:
                result.insert(0, 1)
                N = N//-2 +1
            else:
                result.insert(0, 0) 
                N //= -2
                
        print("".join(map(str, result)))