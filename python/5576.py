import sys

if __name__ == "__main__":
    
    W = [0 for _ in range(10)] # W 대학
    K = [0 for _ in range(10)] # K 대학
    
    # W 대학 점수 입력
    for i in range(10):
        W[i] = int(input())
    
    # K 대학 점수 입력
    for i in range(10):
        K[i] = int(input())
        
    w_score = 0
    k_score = 0
    
    for i in range(3):
        max_value = max(W)
        w_score += max_value
        W.remove(max_value)
        
        max_value = max(K)
        k_score += max_value
        K.remove(max_value)
        
    # 출력
    print(w_score, k_score)
    
    