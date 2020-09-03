import math
import sys
from bisect import bisect_right


def init(start, end, node, index, value):
    if index < start or end < index:
        return
    tree[node].append(value)
    if start != end:
        mid = (start + end) // 2
        init(start, mid, node * 2, index, value)
        init(mid + 1, end, node * 2 + 1, index, value)


def find(start, end, node, l, r, k):
    if r < start or l > end:  # 범위를 벗어나면 리턴
        return 0
    elif l <= start and end <= r:  # 구간이 겹침
        return len(tree[node]) - bisect_right(tree[node], k)
    else:
        mid = (start + end) // 2
        return find(start, mid, node * 2, l, r, k) + find(mid + 1, end, node * 2 + 1, l, r, k)


if __name__ == "__main__":
    n = int(sys.stdin.readline())  # 수열의 크기
    num = list(map(int, sys.stdin.readline().split()))  # 수열 입력받기
    m = int(sys.stdin.readline())  # 쿼리의 개수
    tree = [[] for _ in range(int(math.pow(2, math.ceil(math.log2(n) + 1)) - 1))]

    for i in range(n):  # 작은 값 부터 세그먼트 트리를 구성하기 위해서 정렬
        num[i] = [num[i], i + 1]
    num.sort()
    num = [0] + num

    # 세그먼트 트리 초기 구성
    for i in range(1, n + 1):
        init(1, n, 1, num[i][1], num[i][0])

    last_ans = 0
    for _ in range(m):
        q = list(map(int, sys.stdin.readline().split()))
        q[0] = q[0] ^ last_ans
        q[1] = q[1] ^ last_ans
        q[2] = q[2] ^ last_ans
        answer = find(1, n, 1, q[0], q[1], q[2])  # start, end, node, l, r
        print(answer)
        last_ans = answer
