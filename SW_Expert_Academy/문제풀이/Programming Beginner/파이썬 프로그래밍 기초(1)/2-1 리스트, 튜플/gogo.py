#list 구구단 중 3의 배수이거나 7의 배수 제거

result = []


for i in range(2, 10):
    each_gogo = []
    for j in range(1, 10):
        val = i * j
        if val % 3 == 0 or val %7 == 0:
            continue
        else:
            each_gogo.append(val)
        
    result.append(each_gogo)
    
print(result)

