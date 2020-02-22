#github blog : jjangsungwon.github.io
#baekjoon : 18230
import sys

sys.setrecursionlimit(10 ** 8)
N, A, B = map(int, sys.stdin.readline().split())
data_A = list(map(int, sys.stdin.readline().split()))
data_B = list(map(int, sys.stdin.readline().split()))

data_A.sort(reverse = True)
data_B.sort(reverse = True)

value = 0
area = 0
A_idx = 0
B_idx = 0
max_area = 0

check = N // 2

for i in range(check):
    if i <= len(data_B) - 1:
        value += data_B[B_idx]
        B_idx += 1
    else:
        break

area = N - B_idx * 2

# 남은 공간 1개 짜리로 다 채운다
for i in range(area):
    if i <= len(data_A) - 1:
        value += data_A[A_idx]
        A_idx += 1
    else:
        break

max_area = value

# 2개 채운 거를 1개 짜리로 바꾸면서 업데이트한다
B_idx -= 1
while B_idx >= 0:
    if A_idx+1 <= len(data_A)-1:
        value -= data_B[B_idx]
        value += data_A[A_idx] + data_A[A_idx+1]

        if value > max_area:
            max_area = value
            A_idx += 2
            B_idx -= 1
        elif value == max_area:
            B_idx -= 1
        else:
            break
    else:
        break
print(max_area)



