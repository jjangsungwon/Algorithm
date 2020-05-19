import math

if __name__ == "__main__":

    cnt = 1
    while True:
        a, b, c = map(int, input().split())

        if a == 0 and b == 0 and c == 0:
            break

        print("Triangle #{}".format(cnt))
        if a == -1:
            if b >= c:
                print("Impossible.")
            else:
                print("a = %.3f" % (math.sqrt(c * c - b * b)))
        elif b == -1:
            if a >= c:
                print("Impossible.")
            else:
                print("b = %.3f" % (math.sqrt(c * c - a * a)))
        elif c == -1:
            print("c = %.3f" % (math.sqrt(a * a + b * b)))
        print()
        cnt += 1
