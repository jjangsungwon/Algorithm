if __name__ == "__main__":

    N = int(input())

    if N == 0:
        print("divide by zero")
    else:
        num = list(map(int, input().split()))
        result_1 = sum(num) / N
        result_2 = 0

        copy_num = list(set(num))
        for i in range(len(copy_num)):
            result_2 += copy_num[i] * num.count(copy_num[i]) / len(num)

        print("%.2f" % (result_1 / result_2))
