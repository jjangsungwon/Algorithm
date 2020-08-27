import sys

if __name__ == "__main__":
    
    T = int(input())
    
    for i in range(T):
        A, B = map(str, input().split())
        result = []
        
        for i in range(len(A)):
            x, y = ord(A[i]), ord(B[i])
            
            if y >= x:
                result.append(y-x)
            else:
                result.append(y+26-x)
        
        print("Distances: " + " ".join(map(str, result)))
    
    