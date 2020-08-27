# 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하시오(if문 사용)
# 출력예시 1(은)는 9의 약수입니다.

num = int(input())

for n in range(1, num + 1):
    if num % n:
        pass
    else:
        print(format(n)+'(은)는',format(num)+'의 약수입니다.')
