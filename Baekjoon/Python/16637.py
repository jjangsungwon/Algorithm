def calcul(array):
    array = list(array)
    remove_paren = ""  # 괄호 제외한 array 값
    index = 0
    flag = False
    temp = ""
    check = True

    # 괄호 먼저 계산
    while index < len(array):
        check = True
        if flag and array[index] != ")":
            temp += array[index]
        if array[index] == "(":
            flag = True
        elif array[index] == ")":
            flag = False
            sub_sum = eval(temp)
            temp = ""
            if sub_sum < 0:
                remove_paren += str(int(1e9) - sub_sum)
            else:
                remove_paren += str(sub_sum)
            check = False
        if not flag and check:
            remove_paren += array[index]
        index += 1
    result_list = []
    value = ""
    for i in range(len(remove_paren)):
        if remove_paren[i] not in ["+", "-", "*"]:
            value += remove_paren[i]
        else:
            if int(value) > int(1e9):
                value = -(int(value) - int(1e9))
            result_list.append(value)
            result_list.append(remove_paren[i])
            value = ""
    if value != "":
        if int(value) > int(1e9):
            value = -(int(value) - int(1e9))
        result_list.append(value)

    result = int(result_list[0])
    for i in range(1, len(result_list) - 1, 2):
        if result_list[i] == "+":
            result += int(result_list[i + 1])
        elif result_list[i] == "-":
            result -= int(result_list[i + 1])
        elif result_list[i] == "*":
            result *= int(result_list[i + 1])
    return result


def dfs(index, num_list, flag):
    global answer
    if index == n - 1:
        num_list += formula[index]
        if flag:
            num_list += ')'
        answer = max(answer, calcul(num_list))
        return

    # 괄호를 추가하는 경우
    if flag:  # 이미 괄호를 추가했으면 무조건 삭제해야한다.
        num_list += formula[index]
        num_list += ')'
        num_list += formula[index + 1]
        dfs(index + 2, num_list, False)
    else:
        num_list += '('
        num_list += formula[index]
        num_list += formula[index + 1]
        dfs(index + 2, num_list, True)
        num_list = num_list[:-3]

        # 그냥 지나가는 경우
        num_list += formula[index]
        num_list += formula[index + 1]
        dfs(index + 2, num_list, False)


if __name__ == "__main__":
    n = int(input())  # 수식의 길이
    formula = list(input().strip())  # 수식

    if n == 1:  # 숫자의 길이가 1인 경우
        print(formula[0])
    else:
        answer = -1e9
        dfs(0, "", False)
        print(answer)
