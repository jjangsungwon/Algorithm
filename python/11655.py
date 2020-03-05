import sys

if __name__ == "__main__":
    data = sys.stdin.readline()
    arr = []
    #print(ord('a'), ord('z'), ord('A'), ord('Z'))
    # 95, 65, 122, 90

    for i in range(len(data)):
        if 122 >= ord(data[i]) >= 97:   # 소문자
            if ord(data[i]) <= 109:
                arr.append(chr(ord(data[i]) + 13))
            else:
                arr.append(chr(97 + (12 - (122 - ord(data[i])))))
        elif 90 >= ord(data[i]) >= 65:  # 대문자
            if ord(data[i]) <= 77:
                arr.append(chr(ord(data[i]) + 13))
            else:
                arr.append(chr(65 + (12 - (90 - ord(data[i])))))
        else:
            arr.append(data[i])
    print("".join(arr))