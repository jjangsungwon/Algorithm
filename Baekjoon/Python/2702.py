import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)


if __name__ == "__main__":
    
    T = int(input())
    
    for i in range(T):
        a, b = map(int, input().split())
        
        print((a * b) // math.gcd(a, b), math.gcd(a, b))
        