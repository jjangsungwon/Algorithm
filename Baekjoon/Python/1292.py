import math

if __name__ == "__main__":

    A, B = map(int, input().split())

    idx = 1
    limit = 1
    total = 0
    temp = 0
    count = 0
    for i in range(1, B + 1):
        if i >= A:
            total += idx
        temp += idx

        if temp >= limit:
            idx = math.sqrt(limit) + 1
            limit = math.pow(math.sqrt(limit) + 1, 2)
            temp = 0

    print(int(total))
