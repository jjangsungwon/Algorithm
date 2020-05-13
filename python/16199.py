if __name__ == "__main__":

    year, month, day = map(int, input().split())
    o_year, o_month, o_day = map(int, input().split())

    if o_month > month or o_month == month and o_day >= day:
        A = o_year - year
    else:
        A = o_year - year - 1
    B = o_year - year + 1
    C = o_year - year

    print(A)
    print(B)
    print(C)