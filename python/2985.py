if __name__ == "__main__":

    A, B, C = map(int, input().split())

    if A + B == C:
        print("{}+{}={}".format(A, B, C))
    elif A - B == C:
        print("{}-{}={}".format(A, B, C))
    elif A * B == C:
        print("{}*{}={}".format(A, B, C))
    elif A / B == C:
        print("{}/{}={}".format(A, B, C))
    elif A == B + C:
        print("{}={}+{}".format(A, B, C))
    elif A == B - C:
        print("{}={}-{}".format(A, B, C))
    elif A == B * C:
        print("{}={}*{}".format(A, B, C))
    elif A == B / C:
        print("{}={}/{}".format(A, B, C))
