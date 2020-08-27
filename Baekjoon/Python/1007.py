import math
import sys
from itertools import combinations


INF = 1e9
if __name__ == "__main__":
    for tc in range(int(input())):  # 테스트 케이스만큼 반복
        n = int(input())  # 점의 개수
        coordinate = [list(map(int, input().split())) for _ in range(n)]  # 좌표 리스트

        # x와 y의 총합 계산
        total_x, total_y = 0, 0
        for x, y in coordinate:
            total_x += x
            total_y += y

        min_value = sys.maxsize
        for data in list(combinations(coordinate, n // 2)):  # n // 2개 선택
            sub_x, sub_y = 0, 0
            for x, y in data:
                sub_x += x
                sub_y += y
            result_x = total_x - sub_x * 2
            result_y = total_y - sub_y * 2

            min_value = min(min_value, math.sqrt(result_x * result_x + result_y * result_y))
        print('%.12f' % min_value)