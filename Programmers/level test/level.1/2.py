def solution(arr, divisor):
    answer = []

    for data in arr:
        if data % divisor == 0:
            answer.append(data)

    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()

    return answer