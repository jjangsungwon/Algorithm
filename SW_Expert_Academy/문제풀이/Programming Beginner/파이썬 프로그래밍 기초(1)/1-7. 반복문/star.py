#별찍기

line = 1
i = 0
j = 1

while line <= 5:
    # 공백
    while j <= i:
        print(" ", end='')
        j += 1

    j = 1
    # 별
    while j <= (7-2*i):
        if( j+1 <= (7-2*i)):
            print("*", end='')
        else:
            print("*")
        j += 1
    line += 1
    i += 1
    j = 1