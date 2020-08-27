if __name__ == "__main__":
    
    L, P = map(int, input().split())
    total = P * L
    result = []
    
    
    data_list = list(map(int, input().split()))
    
    for i in range(5):
        result.append(data_list[i] - total)
    
    print(" ".join(map(str, result)))
        