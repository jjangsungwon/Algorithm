# boj 1188 음식 평론가
# github blog : jjangsungwon.github.io


def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


if __name__ == "__main__":

    # input
    N, M = map(int, input().split())

    # gcd
    gcd_value = gcd(N, M)

    # 한 사람은 N/M씩 가져간다.
    # 즉 K 명일때 K * (N/M) 이며 이 값이 정수일때는 자르지 않아도 된다.
    # N과 M을 최대공약수로 나눈 후 K가 M'의 배수일때는 자르지 않아도 된다.
    gcd_M = M // gcd_value  # M' 값

    # M'의 배수 계산
    cnt = 0
    for i in range(gcd_M, M + 1):
        if i % gcd_M == 0:
            cnt += 1

    result = M - cnt  # 모두 자른다고 가정 하고 배수 개수만큼 빼준다.
    print(result)
