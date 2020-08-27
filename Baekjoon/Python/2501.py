if __name__ == "__main__":
    N, K = map(int, input().split())
    result = []
    
    idx = 1
    while True:
        if idx * idx > N:
            break
        
        if idx == N:
            result.append(idx)
        elif N % idx == 0:
            result.append(idx)
            result.append(N//idx)
        idx += 1
    
    result = list(set(result))
    result.sort()
    if len(result) < K:
        print(0)
    else:
        print(result[K-1])