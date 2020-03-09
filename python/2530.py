if __name__ == "__main__":
    
    H, M, S = map(int, input().split())
    n = int(input())
    
    total = H * 3600 + M * 60 + S + n
    
    H = total // 3600
    H %= 24
    total %= 3600

    M = total // 60
    M %= 60
    total %= 60
    
    S = total // 1
    
    print(H, M, S)
    