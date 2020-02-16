N, M = map(int, input().split())
card = list(map(int, input().split()))

result = []
real_sum = 1

# 첫 번째 숫자를 넣는다
result.append(card[0])
count = 1
idx = 1
real_sum = 0

if len(card) == 3:
    print(sum(card))
    exit()
else:
    for i in range(N - 2):
        result.clear()
        result.append(card[i])
        idx = i + 1
        check = 2
        while idx <= len(card):
            if len(result) == 3:
                if sum(result) == M:
                    real_sum = sum(result)
                    print(real_sum)
                    exit()
                else:
                    if real_sum < sum(result) <= M:
                        real_sum = sum(result)

                    if idx == len(card)-1:
                        result.clear()
                        result.append(card[i])
                        idx = i + check
                        check = check + 1
                    else:
                        result.pop()
            else:
                if idx < len(card):
                    result.append(card[idx])
                idx += 1
    print(real_sum)
