if __name__ == "__main__":
    
    N = list(map(int, input()))
    N.sort(reverse = True)
    
    if 0 not in N:
        print(-1)
    else:
        sum_digit = 0
        for i in N:
            sum_digit += i

        if sum_digit % 3 == 0:
            print("".join(map(str, N)))
        else:
            print(-1)
