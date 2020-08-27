# github blog : jjangsungwon.github.io
# baekjoon : 1018
import sys

chess = []
N, M = map(int, sys.stdin.readline().split())

for i in range(N):
    data = list(sys.stdin.readline())
    chess.append(data)

cnt = 0
min_cnt = 100000

white = 'W'
black = 'B'

# 전부 돌면서 검사 (0,0 기준)
for k in range(N-7):
    for l in range(M - 7):
        cnt = 0
        for i in range(k, k + 8):
            for j in range(l, l + 8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        if chess[i][j] != white:
                            cnt += 1
                    else:
                        if chess[i][j] != black:
                            cnt += 1
                else:
                    if j % 2 == 0:
                        if chess[i][j] != black:
                            cnt += 1
                    else:
                        if chess[i][j] != white:
                            cnt += 1
        if min_cnt > cnt:
            min_cnt = cnt

for k in range(N-7):
    for l in range(M - 7):
        cnt = 0
        for i in range(k, k + 8):
            for j in range(l, l + 8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        if chess[i][j] != black:
                            cnt += 1
                    else:
                        if chess[i][j] != white:
                            cnt += 1
                else:
                    if j % 2 == 0:
                        if chess[i][j] != white:
                            cnt += 1
                    else:
                        if chess[i][j] != black:
                            cnt += 1
        if min_cnt > cnt:
            min_cnt = cnt

print(min_cnt)


