if __name__ == "__main__":
    string = input()  # 문서
    search_string = input()  # 검색하고 싶은 단어
    answer = 0  # 단어의 횟수

    index = 0
    while index <= len(string) - len(search_string):
        if string[index:index + len(search_string)] == search_string:
            answer += 1
            index += len(search_string)
        else:
            index += 1

    print(answer)