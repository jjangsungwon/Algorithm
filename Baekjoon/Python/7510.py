if __name__ == "__main__":

    N = int(input())

    for i in range(1, N + 1):
        num = list(map(int, input().split()))
        num.sort()
        print("Scenario #{}:".format(i))
        if pow(num[2], 2) == pow(num[0], 2) + pow(num[1], 2):
            print("yes\n")
        else:
            print("no\n")