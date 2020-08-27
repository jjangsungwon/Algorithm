# 1 - 가위 2 - 바위 3 - 보
# 같은 카드인 경우 번호가 작은 쪽을 승자

T = int(input())


def check(a, b, card):
    if card[a] is card[b]:
        return a
    if card[a] is 1:
        if card[b] is 2:
            return b
        else:
            return a
    elif card[a] is 2:
        if card[b] is 3:
            return b
        else:
            return a
    else:
        if card[b] is 1:
            return b
        else:
            return a


def rec(start, end, card):
    if start is end:
        return start
    l = rec(start, (start + end) // 2, card)
    r = rec((start + end) // 2 + 1, end, card)
    return check(l, r, card)


if __name__ == "__main__":
    for tc in range(1, T + 1):
        N = int(input())
        card = list(map(int, input().split()))
        print("#{0} {1}".format(tc, rec(0, N-1, card)+1))
