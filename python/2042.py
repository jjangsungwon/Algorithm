# boj 2042
# blog: jjangsungwon.tistory.com

import sys

tree = [0] * 3000000


# 세그먼트 트리 생성
# start: 시작 인덱스, end: 끝 인덱스
def init(start, end, node, a):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2, a) + init(mid + 1, end, node * 2 + 1, a)
    return tree[node]


# 구간 합 계산
# left, right: 구간 합을 구하고자 하는 범위
# start: 시작 인덱스, end: 끝 인덱스
def sum(start, end, node, left, right):  # left, right: 구간 합을 구하고자 하는 범위
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return sum(start, mid, node * 2, left, right) + sum(mid + 1, end, node * 2 + 1, left, right)


# 값 업데이트
# start: 시작 인덱스, end: 끝 인덱스
# index: 구간 합을 수정하고자 하는 노드
# dif: 수정할 값
def update(start, end, node, index, dif):
    if index < start or index > end:
        return
    tree[node] += dif
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, index, dif)
    update(mid + 1, end, node * 2 + 1, index, dif)


if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split())
    num_list = [int(sys.stdin.readline()) for _ in range(N)]

    init(0, N - 1, 1, num_list)
    for _ in range(M + K):
        a, b, c = map(int, input().split())
        if a == 1:  # b번째 수 c로 바꾸기
            val = c - num_list[b - 1]
            update(0, N - 1, 1, b - 1, val)
            num_list[b - 1] = c
        else:  # b ~ c 합 구하기
            print(sum(0, N - 1, 1, b - 1, c - 1))
