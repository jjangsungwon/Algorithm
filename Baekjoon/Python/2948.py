import sys

if __name__ == "__main__":
    
    calendar = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    D, M = map(int, input().split())
    
    # 달 계산
    for i in range(1, M):
        total += calendar[i]
    
    # 일 계산
    total += D
    
    # 0 - 목요일
    if total % 7 == 1:
        print("Thursday")
    elif total % 7 == 2:
        print("Friday")
    elif total % 7 == 3:
        print("Saturday")
    elif total % 7 == 4:
        print("Sunday")
    elif total % 7 == 5:
        print("Monday")
    elif total % 7 == 6:
        print("Tuesday")
    elif total % 7 == 0:
        print("Wednesday")
        