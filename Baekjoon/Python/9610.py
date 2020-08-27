import sys

if __name__ == "__main__":
    N = int(input())
   
    num1 = 0 #1사분면
    num2 = 0
    num3 = 0
    num4 = 0
    axis = 0
    
    for i in range(N):
        x, y = map(int, input().split())
        
        if x == 0 or y == 0:
            axis += 1
            continue
            
        if x > 0:
            if y > 0:
                num1 += 1
            elif y < 0:
                num4 += 1
        elif x < 0:
            if y > 0:
                num2 += 1
            elif y < 0:
                num3 += 1
    
    print('Q1: {0}'.format(num1))
    print('Q2: {0}'.format(num2))
    print('Q3: {0}'.format(num3))
    print('Q4: {0}'.format(num4))
    print('AXIS: {0}'.format(axis))
    
    