import sys

if __name__ == "__main__":
    
    while True:
        n1, n2 = map(int, input().split())
        
        if n1 == n2:
            break
            
        if n2 % n1 == 0:
            print("factor")
        elif n1 % n2 == 0:
            print("multiple")
        else:
            print("neither")