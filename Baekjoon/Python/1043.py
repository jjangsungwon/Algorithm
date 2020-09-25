import copy


if __name__ == "__main__":
    n, m = map(int, input().split())
    know = list(map(int, input().split()))

    if know[0] == 0:  # 진실을 아는 사람이 없는 경우
        for _ in range(m):
            party = list(map(int, input().split()))
        print(m)  # 모든 파티에서 과장해서 이야기할 수 있다.
    else:
        party = [list(map(int, input().split())) for _ in range(m)]
        know_set = set(know[1:])

        while True:
            pre_length = copy.deepcopy(know_set)
            for i in range(m):
                temp = party[i]
                if temp[0] == 0:
                    continue
                else:
                    flag = False
                    for j in range(1, temp[0] + 1):
                        if temp[j] in know_set:
                            flag = True
                    if flag:
                        for j in range(1, temp[0] + 1):
                            know_set.add(temp[j])

            if len(pre_length) == len(know_set):
                break

        answer = 0
        for i in range(m):
            temp = party[i]
            if temp[0] == 0:
                answer += 1
            else:
                flag = True
                for j in range(1, temp[0] + 1):
                    if temp[j] in know_set:
                        flag = False
                        break
                if flag:
                    answer += 1
        print(answer)