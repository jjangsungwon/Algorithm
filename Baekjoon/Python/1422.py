import sys


def sorting(a, length):  # 가장 긴 숫자와 길이를 일치시켜 준다.
    dif = length - len(a)
    for _ in range(dif):
        a += '1'
    return a


if __name__ == "__main__":
    k, n = map(int, sys.stdin.readline().strip().split())
    q = []
    max_length = -1  # 가장 긴 숫자의 길이
    for _ in range(k):
        num = sys.stdin.readline().strip()
        q.append(num)
        max_length = max(max_length, len(num))

    # 삽입할 숫자 후보 (max_length와 같은 길이를 가지는 것)
    insert_num = []
    for i in range(k):
        if len(q[i]) == max_length:
            insert_num.append(q[i])

    # 삽입할 숫자 후보 중에서 가장 큰 숫자 찾기
    for i in range(len(insert_num)):
        for j in range(len(insert_num)):
            if i != j:
                a = insert_num[i] + insert_num[j]
                b = insert_num[j] + insert_num[i]
                if a < b:
                    insert_num[i], insert_num[j] = insert_num[j], insert_num[i]

    # 삽입할 숫자
    final_insert_num = insert_num[-1]

    # 숫자 삽입
    for _ in range(n - k):
        q.append(final_insert_num)

    # 정렬
    for i in range(len(q)):
        for j in range(len(q)):
            if i != j:
                a = q[i] + q[j]
                b = q[j] + q[i]
                if a < b:
                    q[i], q[j] = q[j], q[i]

    # 숫자 하나씩 출력
    while q:
        num = q.pop()
        print(num, end="")