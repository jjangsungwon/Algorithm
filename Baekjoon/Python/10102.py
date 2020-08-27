import sys

if __name__ == "__main__":
    N = int(input())
    
    a_count = 0
    b_count = 0
    
    result_list = sys.stdin.readline().strip()
    
    for i in result_list:
        if i == "A":
            a_count += 1
        else:
            b_count += 1
            
    
    if a_count > b_count:
        print('A')
    elif a_count < b_count:
        print('B')
    else:
        print('Tie')