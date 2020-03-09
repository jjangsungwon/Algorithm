
if __name__ == "__main__":
    
    unit = [25, 10, 5, 1]
    
    T = int(input())
    
    for i in range(T):
        coin = [0, 0, 0, 0]
        money = int(input())
        
        idx = 0
        while idx != 4:
            if money - unit[idx] >=0:
                money -= unit[idx]
                coin[idx] += 1
            else:
                idx += 1
        
        print(" ".join(map(str, coin)))
    
    