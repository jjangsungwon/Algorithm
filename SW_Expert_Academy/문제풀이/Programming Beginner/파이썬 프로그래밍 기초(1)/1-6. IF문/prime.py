# 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하시오(if문 사용)
# 출력예시 1(은)는 9의 약수입니다.

num = int(input())
result = []

for n in range(1, num + 1):
    if num % n:
        pass
    else:
        print(format(n)+'(은)는',format(num)+'의 약수입니다.')
        result.append(n)

if len(result) == 2:
    print(format(num)+'(은)는', format(result[0])+'과', format(result[1])+'로만 나눌 수 있는 소수입니다.')
