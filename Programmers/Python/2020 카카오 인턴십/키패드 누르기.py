location = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1],
            6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1]}


def solution(numbers, hand):
    left_location, right_location = [3, 0], [3, 2]
    answer = ''

    # 숫자의 범위가 크지 않으므로, 숫자 하나씩 탐색
    for num in numbers:
        if num in [1, 4, 7]:  # 무조건 왼손으로 눌러야 한다.
            answer += "L"
            left_location = location[num]
        elif num in [3, 6, 9]:  # 무조건 오른손으로 눌러야 한다.
            answer += "R"
            right_location = location[num]
        else:
            left_distance = abs(left_location[0] - location[num][0]) + abs(left_location[1] - location[num][1])
            right_distance = abs(right_location[0] - location[num][0]) + abs(right_location[1] - location[num][1])
            if left_distance < right_distance:  # 왼손이 가까운 경우
                answer += "L"
                left_location = location[num]
            elif left_distance > right_distance:  # 오른손이 가까운 경우
                answer += "R"
                right_location = location[num]
            else:
                if hand == "left":
                    answer += "L"
                    left_location = location[num]
                else:
                    answer += "R"
                    right_location = location[num]

    return answer

