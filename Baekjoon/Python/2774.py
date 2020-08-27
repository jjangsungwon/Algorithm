if __name__ == "__main__":
    
    T = int(input())
    
    for i in range(T):
        num = [0 for _ in range(10)]
        data = input()
        cnt = 0
        
        for i in range(len(data)):
            num[int(data[i])] += 1

        for i in range(10):
            if num[i] != 0:
                cnt += 1
        
        print(cnt)