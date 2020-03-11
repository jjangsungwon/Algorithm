if __name__ == "__main__":
    
    N, M, K = map(int, input().split())
    
    # 무조건 여자를 빼는 것이 좋다.
    
    cnt = 0
    while True:
        if N >= 2 and M >= 1:
            N -= 2
            M -= 1
            cnt += 1
        else:
            break
    
    if K <= N + M:
        print(cnt)
        exit()
    else:
        while K > N + M:
            N += 2
            M += 1
            cnt -= 1
    
    print(cnt)
    
    
    
    