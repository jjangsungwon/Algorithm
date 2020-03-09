if __name__ == "__main__":
    
    data = []
    total = 0
    index = []
    
    for i in range(8):
        data.append(int(input()))
    
    for i in range(5):
        max_val = max(data)
        index_val = data.index(max_val)
        
        total += max_val
        index.append(index_val + 1)
        data[index_val] = -1    # 중복 방지
        
        
    index.sort()
    print(total)
    print(" ".join(map(str, index)))
        