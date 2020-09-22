from collections import Counter
from bisect import bisect_left, bisect_right


if __name__ == "__main__":
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]

    ab = []
    cd = []

    # ab 가능한 합 계산
    for i in range(n):
        for j in range(n):
            value = array[i][0] + array[j][1]
            ab.append(value)

    # cd 가능한 합 계산
    for i in range(n):
        for j in range(n):
            value = array[i][2] + array[j][3]
            cd.append(value)

    ab.sort()
    cd.sort()

    answer = 0
    for i in range(len(ab)):
        left_index = bisect_left(cd, -ab[i])
        right_index = bisect_right(cd, -ab[i])
        answer += (right_index - left_index)

    print(answer)
