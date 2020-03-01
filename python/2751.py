import sys

PLUS = 1000000


def counting_sort(data):
    for i in range(len(data)):
        data[i] += PLUS

    length = max(data)
    num_data = [0 for _ in range(length + 1)]
    sum_data = [0 for _ in range(length + 1)]

    for i in data:
        num_data[i] = num_data[i] + 1

    val = num_data[0]
    sum_data[0] = val

    for i in range(1, length + 1):
        sum_data[i] = val + num_data[i]
        val = sum_data[i]

    sort_data = [0 for _ in range(len(data))]
    idx = length

    while True:
        if idx < 0:
            break

        if num_data[idx] > 0:
            sort_data[sum_data[idx] - 1] = idx
            num_data[idx] -= 1
            sum_data[idx] -= 1
        else:
            idx -= 1

    for data in sort_data:
        print(data - PLUS)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    pre_data = []

    for i in range(N):
        data = int(sys.stdin.readline())
        pre_data.append(data)

    counting_sort(pre_data)
