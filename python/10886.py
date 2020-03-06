import sys

if __name__ == "__main__":
    N = int(input())
    yes_cnt = 0
    no_cnt = 0
    
    for i in range(N):
        answer = int(input())
        
        if answer == 1:
            yes_cnt += 1
        else:
            no_cnt += 1
            
    
    if yes_cnt > no_cnt:
        print("Junhee is cute!")
    else:
        print("Junhee is not cute!")
    
