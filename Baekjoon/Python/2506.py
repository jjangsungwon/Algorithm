if __name__ == "__main__":
    
    N = int(input())
    data_list = list(map(int, input().split()))
    
    score = 1
    total = 0
    
    for i in range(N):
        if data_list[i] == 1:
            total += score
            score += 1
        else:
            score = 1
    
    print(total)