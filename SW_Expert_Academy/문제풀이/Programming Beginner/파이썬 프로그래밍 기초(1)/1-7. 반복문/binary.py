# 숫자 사용 횟수

num = int(input())
result = []


while num > 0:
    val = num % 2
    result.insert(0, val)
    num = num //2

print("".join(map(str,result)))
