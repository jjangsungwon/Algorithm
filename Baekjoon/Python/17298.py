import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    stack = []
    result = [-1 for _ in range(N)]

    for i in range(len(data)):
        while stack and data[stack[-1]] < data[i]:
            result[stack.pop()] = data[i]
                
        stack.append(i)
    print(" ".join(map(str, result)))