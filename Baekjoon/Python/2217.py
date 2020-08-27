import sys

if __name__ == "__main__":
    
    N = int(sys.stdin.readline())
    data = []
    
    for i in range(N):
        data.append(int(sys.stdin.readline()))
    
    data.sort(reverse = True)
    
    total = 0
    for i in range(len(data)):
        if total < data[i] * (i+1):
            total = data[i] * (i+1)
    
    print(total)
                   
                   
    
    