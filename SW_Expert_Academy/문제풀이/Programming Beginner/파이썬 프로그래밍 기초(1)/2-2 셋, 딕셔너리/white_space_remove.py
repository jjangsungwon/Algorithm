# 리스트의 원소를 키로 하고, 그 원소의 length를 값으로 갖는 딕셔너리 객체를 생성하는 코드 작성

# data_list
fruit = ['   apple    ','banana','  melon']

# 공백제거 - strip()
dic = {fruit[i].strip() : len(fruit[i].strip())  for i in range(len(fruit))}
print(dic)
