from collections import defaultdict


def solution(table, languages, preference):
    # table을 dictionary 형태로 변환 (key : 직업군, value : 5, 4, 3, 2, 1점 언어)
    table_dict = defaultdict(list)
    for i in range(len(table)):
        temp = table[i].split()
        key = temp[0]
        for j in range(1, 6):
            table_dict[key].append(temp[j])

    # languages 탐색
    score_dict = defaultdict(int)
    for key in table_dict.keys():
        score = 0
        for i in range(len(languages)) :
            if languages[i] in table_dict[key]:
                index = table_dict[key].index(languages[i])
                score += (5 - index) * preference[i]
        score_dict[key] = score

    # 최대 점수 찾기
    max_score = -1
    for key in score_dict:
        max_score = max(max_score, score_dict[key])

    # 직업군 추출
    answer = []
    for key in score_dict:
        if score_dict[key] == max_score:
            answer.append(key)

    # 이름순 정렬
    answer.sort()

    return answer[0]


if __name__ == "__main__":
    print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
                   ["JAVA", "JAVASCRIPT"],
                   [7, 5]))