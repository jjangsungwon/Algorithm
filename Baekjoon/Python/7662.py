import bisect
import sys
from collections import deque


if __name__ == "__main__":
    for _ in range(int(sys.stdin.readline())):
        q = deque()
        n = int(sys.stdin.readline())
        count = dict()
        for _ in range(n):
            order, num = sys.stdin.readline().split()
            num = int(num)
            if order == "I":  # 삽입
                if num in count:
                    count[num] += 1
                else:
                    count[num] = 1
                    bisect.insort_left(q, num)  # 이진 탐색 삽입
            else:  # 삭제
                if len(q) == 0:  # 삭제할 수 있는 숫자가 없는 경우는 명령을 무시한다.
                    continue
                if num == 1:  # 최댓값 삭제
                    if count[q[-1]] > 1:
                        count[q[-1]] -= 1
                    else:
                        del count[q[-1]]
                        q.pop()
                else:  # 최솟값 삭제
                    if count[q[0]] > 1:
                        count[q[0]] -= 1
                    else:
                        del count[q[0]]
                        q.popleft()

        if len(q) == 0:
            print("EMPTY")
        else:
            print(max(q), min(q))

