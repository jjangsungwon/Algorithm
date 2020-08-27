if __name__ == "__main__":

    N = int(input())

    """
    1   2   3   4   5
    9   8   7   6
       10  11  12  13
    17 16  15  14
       18  19  20  21   
    25 24  23  22
    """

    if 1 <= N % 8 <= 5:
        print(N % 8)
    elif N % 8 == 6:
        print(4)
    elif N % 8 == 7:
        print(3)
    elif N % 8 == 0:
        print(2)
