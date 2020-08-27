import sys

if __name__ == "__main__":
    
    # 목표 배수 
    multiple = int(sys.stdin.readline())
    
    while True:
        n = int(sys.stdin.readline())
        
        if n == 0:
            break
            
        if n % multiple == 0: # 배수이면
            print("{} is a multiple of {}.".format(n, multiple))
        else:
            print("{} is NOT a multiple of {}.".format(n, multiple))
        