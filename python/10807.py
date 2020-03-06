import sys

if __name__ == "__main__":
    
    N = int(input())
    data = list(map(int, input().split()))
    object = int(input())
    
    print(data.count(object))