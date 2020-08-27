from collections import deque


if __name__ == "__main__":
    string = input()  # 압축되지 않은 문자열의 길이 출력

    q = deque()

    for i in range(len(string)):
        if string[i] != ")":
            if string[i] == "(":
                q.append(string[i])
            else:
                q.append(int(string[i]))  # 숫자 형태로 반환하여 삽입
        else:  # ")" 기호가 나온 상황
            # "(" 기호를 만날 때까지 숫자의 개수를 센다
            length = 0
            while q:
                value = q.pop()
                if value == "(":
                    break
                else:
                    if value >= 10:
                        length += value - 10
                    else:
                        length += 1
            length = length * q[-1] + 10
            q.pop()  # 마지막 숫자 제거
            q.append(length)

    answer = 0
    for i in range(len(q)):
        if q[i] >= 10:
            answer += q[i] - 10
        else:
            answer += 1
    print(answer)
