import sys

if __name__ == "__main__":
    
    chess = [1, 1, 2, 2, 2, 8]
    data_list = list(map(int, sys.stdin.readline().split()))
    
    # 기존 체스판 말의 개수 - 찾은 말 개수
    for i in range(6):
        chess[i] -= data_list[i]
    
    print(" ".join(map(str, chess)))
    
    