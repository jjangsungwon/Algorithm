import sys

if __name__ == "__main__":
    
    while True:
        M, F = map(int, input().split())
    
        if M == 0 and F == 0:
            break
        else:
            print(M + F)