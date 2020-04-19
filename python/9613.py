import itertools


def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        data = list(map(int, input().split()))
        N = data.pop(0)
        total = 0
        temp = list(itertools.combinations(data, 2))

        for j in range(len(temp)):
            total += gcd(temp[j][0], temp[j][1])

        print(total)