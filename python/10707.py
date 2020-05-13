if __name__ == "__main__":

    # input
    X = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    P = int(input())

    # A사 요금
    A_charge = X * P

    # B사 요금
    if C < P:  # 사용량 넘었을때
        B_charge = B + (P - C) * D
    else:
        B_charge = B

    print(min(A_charge, B_charge))