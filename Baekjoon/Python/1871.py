import math

if __name__ == "__main__":
    
    T = int(input())
    
    for i in range(T):
        car = list(map(str, input().split("-")))
        
        pre_value = 0
        post_value = 0
        
        val = math.pow(26, 2)

        for i in range(3):
            pre_value += (ord(car[0][i]) - 65) * val
            val //= 26
        
        post_value = int(car[1][0] + car[1][1] + car[1][2] + car[1][3])
        
    
        if abs(post_value - pre_value) > 100:
            print("not nice")
        else:
            print("nice")
        
        