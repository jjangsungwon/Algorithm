import sys

if __name__ == "__main__":
    N = int(input())
    
    player1 = 100 # 창영
    player2 = 100 # 상덕
    
    for i in range(N):
        num1, num2 = map(int,input().split())
        
        if num1 == num2:
                continue
        elif num1 > num2:
            player2 -= num1
        else:
            player1 -= num2
            
    
    print(player1)
    print(player2)
    