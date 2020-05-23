if __name__ == "__main__":

    N = int(input())
    N_set = set(list(map(int, input().split())))
    M = int(input())
    M_list = list(map(int, input().split()))

    for i in range(len(M_list)):
        if M_list[i] in N_set:
            print(1, end=" ")
        else:
            print(0, end=" ")
    # # 이분 탐색을 위해 정렬(시간 초과)
    # N_list.sort()
    #
    # while len(M_list) != 0:
    #     val = M_list[0]
    #
    #     left, right = 0, len(N_list) - 1
    #     flag = 0
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if N_list[mid] == val:
    #             flag = 1
    #             print("1", end=" ")
    #             M_list.pop(0)
    #             break
    #         if N_list[mid] < val:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     if flag == 0:
    #         M_list.pop(0)
    #         print("0", end=" ")