T = int(input())


def binary_search(cnt, end, key):
    start = 1
    while start <= end:
        cnt += 1
        middle = (start + end) // 2
        if key == middle:
            return cnt
        elif key < middle:
            end = middle
        else:
            start = middle


for i in range(1, T+1):
    P, A, B = map(int, input().split())
    A_result = binary_search(0, P, A)
    B_result = binary_search(0, P, B)

    if A_result == B_result:
        print("#{0} 0".format(i))
    elif A_result > B_result:
        print("#{0} B".format(i))
    else:
        print("#{0} A".format(i))
