import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    stack = []
    result = [-1 for _ in range(N)]
    cnt = [0 for _ in range(max(data) + 1)]
    
    for d in data:
        cnt[d] += 1
    
    for i in range(len(data)):
        while stack and cnt[data[stack[-1]]] < cnt[data[i]]:
            result[stack.pop()] = data[i]
                
        stack.append(i)
    print(" ".join(map(str, result)))
    
    