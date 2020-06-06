from collections import deque
import sys


if __name__ == "__main__":

    N = int(input())  # 명령의 수
    order = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]

    q = deque()
    count = 0  # 큐에 들어있는 정수의 개수
    # 명령 진행
    for i in range(len(order)):
        if order[i][0] == "push":
            q.append(int(order[i][1]))
            count += 1
        elif order[i][0] == "pop":
            if count == 0:  # 큐에 들어있는 정수가 없는 경우
                print(-1)
            else:
                print(q.popleft())  # pop 결과
                count -= 1
        elif order[i][0] == "size":
            print(count)  # 큐에 들어있는 정수의 개수
        elif order[i][0] == "empty":
            if count == 0:
                print(1)  # 큐가 비어있으면
            else:
                print(0)
        elif order[i][0] == "front":
            if count == 0:
                print(-1)
            else:
                print(q[0])
        elif order[i][0] == "back":
            if count == 0:
                print(-1)
            else:
                print(q[len(q) - 1])
