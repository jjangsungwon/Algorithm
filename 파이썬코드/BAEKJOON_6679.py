result = []


def each_sum(num, base):
    result = 0
    while num > 0:
        result += int(num % base)
        num /= base
    return result


for num in range(1000, 10000):
    copy = num
    a_total = each_sum(num, 10)
    b_total = each_sum(num, 12)
    c_total = each_sum(num, 16)

    if a_total == b_total and b_total == c_total:
        result.append(num)

for i in range(len(result)):
    print(result[i])
