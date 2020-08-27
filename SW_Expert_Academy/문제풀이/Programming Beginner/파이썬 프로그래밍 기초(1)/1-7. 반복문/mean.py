#80점 이상의 점수들의 총합

score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

i = 0
while i < len(score):
    if score[i] < 80:
        score.pop(i)
    else:
        i += 1

print(sum(score))