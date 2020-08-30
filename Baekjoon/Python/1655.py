from bisect import bisect_left

if __name__ == "__main__":
    n = int(input())  # 수빈이가 외치는 정수의 개수 입력받기
    array = []  # 입력받은 숫자를 저장할 리스트 선언

    # 첫 번째 숫자 입력받기
    num = int(input())
    array.append(num)
    print(num)

    # array 현재 길이
    length = 1

    # 두 번째 숫자부터 차례대로 입력받기
    for _ in range(n - 1):
        num = int(input())
        # 숫자가 삽입 될 인덱스 찾기
        index = bisect_left(array, num)
        # 숫자 삽입, array 길이 1 증가
        array.insert(index, num)
        length += 1

        if length % 2 == 0:  # 짝수개
            print(min(array[length // 2 - 1], array[length // 2]))
        else:
            print(array[length // 2])
