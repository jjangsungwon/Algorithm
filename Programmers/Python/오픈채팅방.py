import copy


def solution(record):
    answer = []

    temp = []
    for i in range(len(record)):
        temp.append(record[i].split())

    id = {}
    for i in range(len(temp)):
        if temp[i][0] == "Enter" or temp[i][0] == "Change":
            id[temp[i][1]] = temp[i][2]

    for i in range(len(temp)):
        if temp[i][0] == "Enter":
            answer.append(id[temp[i][1]] + "님이 들어왔습니다.")
        elif temp[i][0] == "Leave":
            answer.append(id[temp[i][1]] + "님이 나갔습니다.")

    return answer


if __name__ == "__main__":
    print(solution(
        ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
