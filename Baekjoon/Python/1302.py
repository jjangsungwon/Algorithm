if __name__ == "__main__":
    N = int(input())
    book = {}

    for _ in range(N):
        book_name = input()
        if book_name not in book.keys():
            book[book_name] = 1
        else:
            book[book_name] += 1

    # 가장 많이 팔린 책의 권수 파악
    answer = 0
    for key in book.keys():
        answer = max(answer, book[key])

    # 가장 많이 팔린 챙의 이름 파악
    result = []
    for key in book.keys():
        if answer == book[key]:
            result.append(key)

    # 사전순 정렬
    result.sort()

    # 출력
    print(result[0])
