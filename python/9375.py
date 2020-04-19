if __name__ == "__main__":

    # input
    T = int(input())

    for _ in range(T):
        N = int(input())  # 가진 의상의 수
        clothes = {}
        for _ in range(N):
            name, kind = map(str, input().split())  # 이름, 종류

            if kind in clothes.keys():
                clothes[kind] += 1  # 기존에 존재하는 종류면 1개 추가
            else:
                clothes[kind] = 1  # 없으면 추가

        result = 1
        keys = clothes.keys()

        if N == 0:
            result = 0
        elif len(clothes) == 1:
            result = 0
            for index in keys:
                result += clothes[index]  # 낱개
        else:
            for index in keys:
                result *= (clothes[index] + 1)  # 조합

            result -= 1  # 안 입는 경우 제외

        print(result)
