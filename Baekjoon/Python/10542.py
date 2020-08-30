if __name__ == "__main__":

    n = int(input())  # 참가자의 수
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)  # 지목값

    for i in range(1, n + 1):
        number = int(input())
        in_degree[number] += 1  # i -> number 지목
        out_degree[i] = number

    mafia = [None] * (n + 1)  # 현재 마피아 정보 모르는 상황
    checked = [False] * (n + 1)

    # in_degree 값이 0인 것은 무조건 마피아. 해당 값이 가르키는 것은 무조건 사람
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            flag = True  # 들어오는 값이 없으므로 마피아라고 둔다.
            index = i
            while True:
                if not checked[index]:  # 아직 확인하지 않았으면
                    checked[index] = True  # 중복 방지를 위해서 체크
                    if flag:
                        mafia[index] = True
                    in_degree[out_degree[index]] -= 1  # 진입 차수 1감소
                    if in_degree[out_degree[index]] == 0 or flag:  # 진입 차수가 0이거나, 현재 값이 마피아이면 한번더 진행한다.
                        if flag:
                            flag = False
                        else:
                            flag = True
                        index = out_degree[index]
                    else:
                        break
                else:
                    break

    # 나머지 마피아 찾기
    for i in range(1, n + 1):
        if not checked[i]:
            flag = False  # 사람으로 가정한다.
            index = i
            while True:
                if not checked[index]:  # 아직 확인하지 않았으면
                    checked[index] = True  # 중복 방지를 위해서 체크
                    if flag:
                        mafia[index] = True
                    in_degree[out_degree[index]] -= 1  # 진입 차수 1감소
                    if in_degree[out_degree[index]] == 0 or flag:  # 진입 차수가 0이거나, 현재 값이 마피아이면 한번더 진행한다.
                        if flag:
                            flag = False
                        else:
                            flag = True
                        index = out_degree[index]
                    else:
                        break
                else:
                    break

    cnt = 0
    for i in range(1, n + 1):
        if mafia[i]:
            cnt += 1

    # 출력
    print(cnt)
