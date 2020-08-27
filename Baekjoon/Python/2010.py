import sys

if __name__ == "__main__":
    
    N = int(sys.stdin.readline())
    data = []
    
    for i in range(N):
        data.append(int(sys.stdin.readline()))
    
    print(sum(data) - N + 1)
    