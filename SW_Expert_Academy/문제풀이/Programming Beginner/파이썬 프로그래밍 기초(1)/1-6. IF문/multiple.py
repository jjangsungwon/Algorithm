#1~200사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자 찾아 콤마로 구분

result = ""
temp = 1

for num in range(1, 201):
    if num % 7 == 0 and num % 5 != 0:
        if temp:
            result += str(num)
            temp = 0
        else:
            result += ','
            result += str(num)

print(result, sep=',')
