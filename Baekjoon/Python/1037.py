
if __name__ == "__main__":

    N = int(input())
    data_list = list(map(int, input().split()))

    data_list.sort()

    print(data_list[0] * data_list[-1])


