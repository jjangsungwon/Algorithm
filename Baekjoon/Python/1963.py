import math, copy
from collections import deque


def prime_check(n):  # n값이 소수인지 확인
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


def bfs(A, B):
    answer = 0
    # 한자리 값을 다루기 위해서 int -> string 변환

    q = deque([[list(str(A)), 0]])
    visited = {A}

    while True:
        val, cnt = q.popleft()
        if int("".join(map(str,val))) == B:
            return cnt
        else:
            for i in range(4):  # 각자리 변환
                for j in range(10):  # 변환 값
                    if val[i] == str(j):
                        continue
                    else:
                        temp = copy.deepcopy(val)
                        temp[i] = str(j)  # 값 변환
                        temp_value = int("".join(map(str, temp)))
                        if temp_value not in visited and temp_value >= 1000 and prime_check(temp_value):  # 조건 확인
                            visited.add(temp_value)
                            q.append([temp, cnt + 1])


if __name__ == "__main__":

    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        print(bfs(A, B))
