if __name__ == "__main__":

    N = int(input())
    N_list = list(map(int, input().split()))
    M = int(input())
    M_list = list(map(int, input().split()))

    for i in range(len(M_list)):
        if M_list[i] in N_list:
            print(1)
        else:
            print(0)
