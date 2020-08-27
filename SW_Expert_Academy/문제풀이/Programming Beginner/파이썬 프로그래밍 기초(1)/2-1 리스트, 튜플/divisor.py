# 약수 구하기

data = int(input())
result = []

for i in range(1, data//2+1):
    if data % i == 0:
        result.append(i)
result.append(data)
print(result)