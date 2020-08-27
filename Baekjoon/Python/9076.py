import sys

if __name__ == "__main__":
    
    T = int(input())

    for i in range(T):
        num = list(map(int, input().split()))
        
        # 최고점 삭제
        index = num.index(max(num))
        del num[index]
        
        # 최저점 삭제
        index = num.index(min(num))
        del num[index]
        
        max_value = max(num)
        min_value = min(num)
        
        if max_value - min_value >=4:
            print("KIN")
        else:
            print(sum(num))