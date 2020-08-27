import sys

if __name__ == "__main__":
    
    N, B = input().split()
    
    B = int(B)
    
    mul = 1
    val = 0
    
    for i in range(len(N)-1, -1, -1):
        if 49 <= ord(N[i]) <= 57:
            val += mul * int(N[i])
        elif  65 <= ord(N[i]) <= 90:
            val += mul * (ord(N[i]) - 55)
        mul *= B
    
    print(val)
    