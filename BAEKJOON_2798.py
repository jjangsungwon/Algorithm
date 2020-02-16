N, M = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0


def dfs(n, idx, cards_sum):
    if idx == 3:
        global answer
        if answer < cards_sum <= M:
            answer = cards_sum
        return

    if n >= len(cards):
        return

    # 현재 카드를 선택하고 내가 가진 카드 중 다음 카드로 넘어간다.
    dfs(n + 1, idx + 1, cards_sum + cards[n])

    # 현재 카드를 선택하지 않고 다음 카드로 넘어간다.
    dfs(n + 1, idx, cards_sum)


dfs(0, 0, 0)
print(answer)