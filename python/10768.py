if __name__ == "__main__":

    month = int(input())
    day = int(input())

    # 2월 18일
    if month == 2 and day == 18:
        print("Special")
    elif (month == 2 and day < 18) or month == 1:
        print("Before")
    else:
        print("After")