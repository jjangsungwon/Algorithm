import sys

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    arr = []
    
    for i in range(N):
        arr.append(N)
        
    data = "".join(map(str, arr))
    
    
    if len(data) >= M:
        print(data[:M])
    else:
        print(data)
    