answer = 0
find_flag = False
vowel = ['A', 'E', 'I', 'O', 'U']


def dfs(depth, current_word, target_word):
    global answer, find_flag

    if current_word == target_word:
        find_flag = True
        return

    for i in range(5):
        if find_flag is False:
            if depth + 1 < 6:
                answer += 1
                dfs(depth + 1, current_word + vowel[i], target_word)


def solution(word):
    dfs(0, "", word)
    return answer


if __name__ == "__main__":
    print(solution("AAAAE"))
    # print(solution("AAAE"))
    # print(solution("I"))
    # print(solution("EIO"))