import copy
from collections import deque
from itertools import permutations


def solution(expression):
    answer = 0
    expression_list = ["" for _ in range(101)]  # 최대 길이 100

    # 연산자의 갯수 파악
    operation = []
    for i in range(len(expression)):
        if expression[i] in ['+', '-', '*']:
            operation.append(expression[i])
    operation = list(set(operation))

    # expression 배열을 리스트 형태로 바꾼다.
    index = 0
    for i in range(len(expression)):
        if expression[i] in operation:
            index += 1
            expression_list[index] = expression[i]
            index += 1
        else:
            expression_list[index] += expression[i]
    expression_list = expression_list[:index + 1]
    copy_expression_list = copy.deepcopy(expression_list)

    # 연산자 가능한 순서 모두 대입(브루트 포스)
    for data in list(permutations(operation, len(operation))):
        expression_list = copy.deepcopy(copy_expression_list)
        for i in range(len(data)):  # 연산자 갯수만큼 반복
            q = deque()
            index = 0
            while index < len(expression_list):
                if expression_list[index] != data[i]:
                    q.append(expression_list[index])
                else:
                    first = q.pop()
                    index += 1
                    q.append(str(eval(first + data[i] + expression_list[index])))
                index += 1
            expression_list = copy.deepcopy(q)
        answer = max(answer, abs(int(expression_list[0])))
    return answer


if __name__ == "__main__":
    print(solution("50*6-3*2"))