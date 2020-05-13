if __name__ == "__main__":

    num = input()

    if num[1] == '0':
        result = int(num[0] + num[1]) + int(num[2:])
    else:
        result = int(num[0]) + int(num[1:])

    print(result)