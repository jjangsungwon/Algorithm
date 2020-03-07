import sys

if __name__ == "__main__":
    N = int(input())
    
    for i in range(N):
        V, E = map(int, input().split())
        
        print(2 - V + E)
    