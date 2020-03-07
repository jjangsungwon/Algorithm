import sys

if __name__ == "__main__":
    
    T = int(input())
    a_count = b_count = c_count = 0
    A, B, C = 300, 60, 10
    
    

    while T >= 300:
        a_count += 1
        T -= 300

    while T >= 60:
        b_count += 1
        T -= 60

    while T >= 10:
        c_count += 1
        T -= 10

    
    if T == 0:
        print(a_count, b_count, c_count)
    else:
        print(-1)