'''
 파이썬을 시작한 지 얼마 되지 않아 코드가  깨끗하지 않을 수 있습니다.
 꾸준히 공부해서 실력을 늘리겠습니다.
'''
S, K = input().split()

S = int(S)
K = int(K)
result = []

result.append(S - (K-1))
for i in range(1, K):
    result.append(1)

mul = 1
for i in (result):
    mul = mul * i

temp_mul = 1
check = 0

while True:
    check = 0
    for i in range(1, K):
        temp = result[:]
        temp[0] = temp[0] - 1
        temp[i] = temp[i] + 1
        temp_mul = 1

        for k in temp:
            temp_mul = temp_mul * k
        if mul < temp_mul:
            mul = temp_mul
            result = temp[:]
            check = 1

    if check == 0:
        break;

mul = 1
for i in (result):
    mul = mul * i
print(mul)
