import sys

if __name__ == "__main__":
    A, B, C, D = map(str, sys.stdin.readline().split())
    
    AB = A + B
    CD = C + D
    
    AB = int(AB)
    CD = int(CD)
    
    print(AB + CD)
    