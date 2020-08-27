import sys

if __name__ == "__main__":
    N = int(input())
    car_list = list(map(int, input().split()))
    
    cnt = 0
    
    for d in car_list:
        if d == N:
            cnt += 1
    
    print(cnt)