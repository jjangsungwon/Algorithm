if __name__ == "__main__":

    first = list(map(int, input().split()))
    second = list(map(int, input().split()))

    print(min(first[0] + second[1], first[1] + second[0]))