
if __name__== "__main__":
    
    A, B = map(int, input().split())
    n = int(input())
    
    total = A * 60 + B + n
    
    A = total // 60
    A %= 24
    total %= 60
    
    B = total // 1
    
    print(A, B)