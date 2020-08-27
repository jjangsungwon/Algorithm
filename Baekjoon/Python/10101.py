if __name__ == "__main__":

    a = int(input())
    b = int(input())
    c = int(input())

    if a + b + c == 180:
        if a == 60 and b == 60 and c == 60:
            print("Equilateral")
        elif a == b != c or a != b == c or a == c != b:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Error")