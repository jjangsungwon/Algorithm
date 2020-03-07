import sys

if __name__ == "__main__":
    T = int(input())
    
    for i in range(T):
        c, p = map(int, input().split())
        
        print('You get {0} piece(s) and your dad gets {1} piece(s).'.format(c//p, c%p))
    