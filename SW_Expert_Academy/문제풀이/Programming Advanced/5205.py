def quick_sort(l, r):
    if l > r:
        return 
    
    p = partition(l, r)
    left = quick_sort(l, p - 1)
    right = quick_sort(p + 1, r)
    
def partition(l, r):
    
    pivot = (l + r) // 2
    
    while l < r:
        while data_list[l] < data_list[pivot] and l < r:
            l += 1
    
        while data_list[r] >= data_list[pivot] and l < r:
            r -= 1
    
        if l < r:
            if l == pivot:
                pivot = r
            data_list[l], data_list[r] = data_list[r], data_list[l]    
    data_list[pivot], data_list[r] = data_list[r], data_list[pivot]
    
    return r

if __name__ == "__main__":
    
    T = int(input())
    
    for tc in range(1, T + 1):
        N = int(input())
        data_list = list(map(int, input().split()))
        
    
        quick_sort(0, N - 1)
        
        print("#{} {}".format(tc, data_list[N//2]))