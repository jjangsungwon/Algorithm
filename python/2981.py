import math


def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def divisor(n):
    result = []

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.append(n // i)
            result.append(i)

    result.sort()
    return result


if __name__ == "__main__":

    N = int(input())
    data = []

    for _ in range(N):
        data.append(int(input()))
    data.sort()
    sub_list = []
    for i in range(N - 1):
        sub_list.append(data[i + 1] - data[i])

    if len(sub_list) == 1:
        answer = sub_list[0]
    elif len(sub_list) == 2:
        answer = gcd(sub_list[0], sub_list[1])
    else:
        answer = sub_list[0]
        for i in range(1, len(sub_list)):
            answer = gcd(answer, sub_list[i])

    answer = divisor(answer)
    answer = list(set(answer))
    answer.sort()
    answer.pop(0)

    print(" ".join(map(str, answer)))
