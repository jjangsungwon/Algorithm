import sys

if __name__ == "__main__":
    
    T = int(input())
    
    for i in range(T):
        operation = list(map(str, input().split()))
        
        n = float(operation[0])
        
        for i in range(1, len(operation)):
            if operation[i] == "@":
                n *=3
            elif operation[i] == "%":
                n += 5
            elif operation[i] == "#":
                n -= 7
        
        print("%.2f" %n)