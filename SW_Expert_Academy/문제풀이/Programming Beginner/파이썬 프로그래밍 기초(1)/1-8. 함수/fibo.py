# 피보나치 수열 결과

def fib(n):
    result = [1, 1]

    if n == 1:
        result.pop()
    elif n == 2:
        pass
    else:
        cnt = 2
        while cnt < n:
            sum = result[cnt - 2] + result[cnt - 1]
            result.append(sum)
            cnt += 1
        return result


n = int(input())

print(fib(n))
