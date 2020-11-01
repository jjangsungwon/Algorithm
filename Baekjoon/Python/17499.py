import sys


if __name__ == "__main__":
    n, q = map(int, sys.stdin.readline().split())  # 수열의 길이, 연산의 개수
    a = list(map(int, sys.stdin.readline().split()))

    first_index = 0
    for _ in range(q):
        order = list(map(int, input().split()))
        if order[0] == 1:  # '+'
            target_index = (first_index + order[1] - 1) % n
            a[target_index] += order[2]
        elif order[0] == 2:  # 'right shift'
            first_index = first_index - order[1]
            if first_index < 0:
                first_index = n + first_index
        else:  # 'left shift'
            first_index = (first_index + order[1]) % n

    # 출력
    for i in range(first_index, n):
        print(a[i], end=" ")
    for i in range(0, first_index):
        print(a[i], end=" ")
