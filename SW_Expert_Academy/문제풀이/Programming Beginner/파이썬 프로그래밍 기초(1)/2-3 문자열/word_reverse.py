# 단어 역순 출력

# data입력
data = input()

# reverse() 함수를 이용하기 위해 list형으로 변형
list_data = data.split(' ')

# 단어 역순
list_data.reverse()

# 출력을 위해서 join 사용
print(" ".join(list_data))