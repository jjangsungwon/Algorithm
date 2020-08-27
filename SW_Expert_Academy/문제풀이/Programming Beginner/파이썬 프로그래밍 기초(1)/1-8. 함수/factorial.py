# 리스트 중복(duplication) 제거

def factorial(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


n = int(input())
print(factorial(n))
