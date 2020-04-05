def divisor(value):
    result = []
    for i in range(1, value // 2 + 1):
        if value % i == 0:
            result.append(i)
            result.append(value // i)

    result = sorted(list(set(result)), reverse=True)
    return result


if __name__ == "__main__":

    n = int(input())
    arr = list(map(int, input().split()))

    radius = arr.pop(0)

    for data in arr:
        copy_radius = radius
        radius_divisor = divisor(radius)
        data_divisor = divisor(data)

        for i in radius_divisor:
            if i in data_divisor:
                if copy_radius % i == 0 and data % i == 0:
                    copy_radius //= i
                    data //= i

        print("{0}/{1}".format(copy_radius, data))
