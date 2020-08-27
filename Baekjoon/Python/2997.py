if __name__ == "__main__":

    num_list = list(map(int, input().split()))

    num_list.sort()
    # 1, 2, 3 순서
    if num_list[1] - num_list[0] == num_list[2] - num_list[1]:
        result = num_list[2] + num_list[2] - num_list[1]
    # 1, 2, 4 순서
    elif (num_list[2] - num_list[1]) // 2 == num_list[1] - num_list[0]:
        result = num_list[1] + num_list[1] - num_list[0]
    # 1, 3, 4 순서
    elif num_list[2] - num_list[1] == (num_list[1] - num_list[0]) // 2:
        result = num_list[0] + num_list[2] - num_list[1]
    # 2, 3, 4 순서
    else:
        result = num_list[0] - num_list[2] - num_list[1]

    print(result)