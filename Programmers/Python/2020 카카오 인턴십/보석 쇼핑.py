def solution(gems):
    total = len(set(gems))
    answer = [0, len(gems) - 1]
    start = 0
    end = 0

    selected = {gems[0]: 1}
    while start < len(gems) and end < len(gems):
        if len(selected) == total:
            if answer[1] - answer[0] > end - start:  # 거리를 좁힐 수 있다면
                answer[0] = start
                answer[1] = end

            # start 제거하고 재시도
            if selected[gems[start]] > 1:
                selected[gems[start]] -= 1
            else:
                del selected[gems[start]]
            start += 1
        else:
            end += 1
            if end == len(gems):
                break

            if selected.get(gems[end]) is None:
                selected[gems[end]] = 1
            else:
                selected[gems[end]] += 1

    answer[0] += 1
    answer[1] += 1
    return answer


if __name__ == "__main__":
    print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
