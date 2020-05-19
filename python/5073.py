if __name__ == "__main__":

    while True:
        n = list(map(int, input().split()))

        if n[0] == 0 and n[1] == 0 and n[2] == 0:
            break

        n.sort(reverse=True)
        if n[0] >= n[1] + n[2]:
            print("Invalid")
        else:
            # 세 변의 길이가 모두 같은 경우
            if n[0] == n[1] == n[2]:
                print("Equilateral")
            # 두 변의 길이가 모두 같은 경우
            elif n[0] == n[1] or n[1] == n[2] or n[0] == n[2]:
                print("Isosceles")
            # 세 변의 길이가 모두 다른 경우
            else:
                print("Scalene")
