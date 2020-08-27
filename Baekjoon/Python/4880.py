if __name__ == "__main__":

    while True:
        a1, a2, a3 = map(float, input().split())
        if a1 == 0 and a2 == 0 and a3 == 0:
            break

        if a2 - a1 == a3 - a2:
            if a2 - a1 != 0:
                print("AP", int(a3 + a3 - a2))
        elif a2 / a1 == a3 / a2:
            if a2 / a1 != 0:
                print("GP", int(a3 * (a3 // a2)))
