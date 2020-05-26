from collections import deque
import sys


if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        operation = input()
        n = int(sys.stdin.readline())
        temp = input()
        temp = temp[1:-1]

        if "," not in temp and temp != "":
            num_deque = deque([int(temp)])
        elif temp != "":
            num_deque = deque(map(int, temp.split(",")))
        else:
            num_deque = deque()

        # 명령 수행
        flag = 1
        cnt = 0  # Reverse의 개수

        for i in range(len(operation)):
            if operation[i] == "R":
                cnt += 1
            else:
                if len(num_deque) == 0:
                    flag = 0
                    break

                if cnt % 2 == 0:
                    num_deque.popleft()
                else:
                    num_deque.pop()
        if cnt % 2 == 1:
            num_deque.reverse()

        if flag:
            print("[", end="")
            for i in range(len(num_deque)):
                if i == len(num_deque) - 1:
                    print(num_deque[i], end="")
                else:
                    print(str(num_deque[i]) + ",", end="")
            print("]")
        else:
            print("error")