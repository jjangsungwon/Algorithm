import sys


if __name__ == "__main__":
    n = int(input())
    array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    a_list, b_list, c_list, d_list = list(), list(), list(), list()
    for i in range(n):
        for j in range(4):
            value = array[i][j]
            if j == 0:
                a_list.append(value)
            elif j == 1:
                b_list.append(value)
            elif j == 2:
                c_list.append(value)
            elif j == 3:
                d_list.append(value)

    ab = dict()

    # ab 가능한 합 계산
    for a in a_list:
        for b in b_list:
            ab[a + b] = ab.get(a + b, 0) + 1

    # cd 가능한 합 계산
    answer = 0
    for c in c_list:
        for d in d_list:
            answer += ab.get(-(c + d), 0)

    print(answer)