def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    global cnt
    
    left_idx, right_idx = 0, 0
    result = []
    
    if left[-1] > right[-1]:
        cnt += 1

    while left_idx < len(left) and right_idx <len(right):
        if left[left_idx] > right[right_idx]:
            result.append(right[right_idx])
            right_idx += 1
        else:
            result.append(left[left_idx])
            left_idx += 1

    if left_idx < len(left):
        while left_idx < len(left):
            result.append(left[left_idx])
            left_idx += 1
    
    if right_idx < len(right):
        while right_idx < len(right):
            result.append(right[right_idx])
            right_idx += 1
            
    return result
    
if __name__ == "__main__":
    
    T = int(input())
    
    for tc in range(1, T + 1):
        N = int(input())
        data_list = list(map(int, input().split()))
        cnt = 0
        
        result_list = merge_sort(data_list)
        print("#{0} {1} {2}".format(tc, result_list[N//2], cnt))
        