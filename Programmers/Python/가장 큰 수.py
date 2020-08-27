def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 4, reverse=True)
    result = "".join(map(str, numbers))

    if int(result) == 0 or result[0] == '0':
        return str(int(result))
    else:
        return result