import sys

if __name__ == "__main__":
    hambuger = 10000
    drink = 10000
    
    for i in range(5):
        d = int(input())
        
        if i<=2:
            if d < hambuger:
                hambuger = d
        else:
            if d < drink:
                drink = d
                
    
    print(hambuger + drink - 50)