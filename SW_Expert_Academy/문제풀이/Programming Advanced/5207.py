def binary_search(obj, l, r, flag):
    global cnt
    if l > r:
        return
    mid = (l + r) // 2
    
    if A[mid] == obj:
        cnt += 1
        return
    else:
        if A[mid] < obj:
            if flag == 1:
                return
            binary_search(obj, mid + 1, r, 1)
        else:
            if flag == -1:
                return
            binary_search(obj, l, mid - 1, -1)

if __name__ == "__main__":
    
    T = int(input())
    
    for tc in range(1, T + 1):
        
        cnt = 0
        a_num, b_num = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
    
        # A 정렬
        A.sort()
        
        for data in B:
            if data in A:
                binary_search(data, 0, a_num - 1, 0)
        
        print("#{} {}".format(tc, cnt))
        
    
    