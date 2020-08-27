if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        robot = list(map(int, input().split()))
        total = robot[0] * 350.34 + robot[1] * 230.90 + robot[2] * 190.55 + robot[3] * 125.30 + robot[4] * 180.90

        print("$%.2f" %total)