if __name__ == "__main__":

    data = list(map(int, input().split()))
    data.sort()

    string = input()

    for i in range(3):
        if string[i] == "A":
            print(data[0], end=" ")
        elif string[i] == "B":
            print(data[1], end=" ")
        else:
            print(data[2], end=" ")
