def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def solution(scores):
    answer = ''

    length = len(scores)

    # 0번 학생부터 학점 계산
    for j in range(length):
        max_score, min_score = [-1, 0], [101, 0]  # 값, 개수
        sum = 0  # 점수 합계
        for i in range(length):
            sum += scores[i][j]
            # 최소점 업데이트
            if scores[i][j] == min_score[0]:  # 최소점과 같은 경우
                min_score[1] += 1
            elif scores[i][j] < min_score[0]:  # 최소점보다 작은 경우
                min_score = [scores[i][j], 1]

            # 최고점 업데이트
            if scores[i][j] == max_score[0]:  # 최고점과 같은 경우
                max_score[1] += 1
            elif scores[i][j] > max_score[0]:  # 최고점보다 큰 경우
                max_score = [scores[i][j], 1]

        # 유일한 최고점 또는 최저점인지 확인
        flag = False
        if scores[j][j] == min_score[0] and min_score[1] == 1:  # 유일한 최저점
            flag = True
        elif scores[j][j] == max_score[0] and max_score[1] == 1:  # 유일한 최고점
            flag = True

        if flag:
            mean_score = (sum - scores[j][j]) / (length - 1)
        else:
            mean_score = sum / length

        answer += grade(mean_score)

    return answer


if __name__ == "__main__":
    print(solution([[100, 90, 98, 88, 65],
                    [50, 45, 99, 85, 77],
                    [47, 88, 95, 80, 67],
                    [61, 57, 100, 80, 65],
                    [24, 90, 94, 75, 65]]))
