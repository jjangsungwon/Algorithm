import sys

if __name__ == "__main__":
    
    A = list(map(int, input().split()))    # 민국이
    B = list(map(int, input().split()))    # 만세
    
    if sum(A) >= sum(B):
        print(sum(A))
    else:
        print(sum(B))