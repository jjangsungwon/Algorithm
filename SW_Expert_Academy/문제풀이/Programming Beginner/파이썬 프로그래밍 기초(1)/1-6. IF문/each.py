#100~300사이의 정수 가운데 각각의 자리 숫자가 짝수인 숫자 찾아 콤마로 구분

result = []

for num in range(100, 301):
    num = str(num)
    if int(num[0]) % 2 == 0:
        if int(num[1]) % 2 == 0:
            if int(num[2]) % 2 == 0:
                result.append(int(num))

print( ",".join(map(str, result)))
