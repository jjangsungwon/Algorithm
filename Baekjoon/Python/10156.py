import sys

if __name__ == "__main__":
    
    K, N, M = map(int, input().split())
    
    if M - (K * N) >=0:
        print(0)
    else:
        print(abs(M - (K *N)))
        