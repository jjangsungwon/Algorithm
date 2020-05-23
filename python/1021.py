if __name__ == "__main__":
    N, M = map(int, input().split())
    pick_list = list(map(int, input().split()))

    cnt = 0  # 뽑은 숫자의 개수
    move = 0  # 연산 횟수
    num_list = [i for i in range(1, N + 1)]

    while cnt != M:
        if num_list[0] == pick_list[0]:
            num_list.pop(0)
            pick_list.pop(0)
        else:
            index = num_list.index(pick_list[0])
            if index <= len(num_list) // 2:  # 오른쪽으로 가는게 좋은 경우
                move += index
            else:  # 왼쪽으로 가는게 좋은 경우
                move += len(num_list) - index
            new_list = num_list[index:]
            new_list.extend(num_list[:index])
            new_list.pop(0)
            num_list = new_list
            pick_list.pop(0)
        cnt += 1
    print(move)
