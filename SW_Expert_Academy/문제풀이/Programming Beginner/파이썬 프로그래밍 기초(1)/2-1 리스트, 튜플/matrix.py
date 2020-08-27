data = input()

# list로 변환
data_list = list(map(int, data.split(",")))
#print(data_list)

# 2차원 배열 구조
result = []
for i in range(data_list[0]):
    temp = []
    for j in range(data_list[1]):
        temp.append(i*j)
    result.append(temp)

print(result)