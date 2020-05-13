import math

if __name__ == "__main__":

    L = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())

    korea = math.ceil(A / C)
    math = math.ceil(B / D)

    if korea >= math:
        print(L - korea)
    else:
        print(L - math)
