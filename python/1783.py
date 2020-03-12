if __name__ == "__main__":
    
    N, M = map(int, input().split())
    
    if N == 1:
        print(1)
    elif N == 2:
        print(min(4, 1 + (M-1)//2))
    else:
        if M >= 7:
            print(M-2)
        elif M >=5:
            print(4)
        else:
            print(M)
            