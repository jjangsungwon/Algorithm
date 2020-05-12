# push, pop 연산은 O(1)이다.
# insert의 연산때문에 시간초과가 발생한 것 같다.
# insert를 append 형태로 바꿔주기 위해서 스택을 2개 구현하였다.

import sys

if __name__ == "__main__":

    left_string = list(sys.stdin.readline().strip())
    right_string = []

    N = int(sys.stdin.readline())

    for i in range(N):
        operation = sys.stdin.readline().split()
        if operation[0] == "L":
            if len(left_string) == 0:
                continue
            right_string.append(left_string.pop())
        elif operation[0] == "D":
            if len(right_string) == 0:
                continue
            left_string.append(right_string.pop())
        elif operation[0] == "B":
            if len(left_string) == 0:
                continue
            left_string.pop()
        elif operation[0] == "P":
            left_string.append(operation[1])

    print("".join(map(str, left_string + right_string[::-1])))
