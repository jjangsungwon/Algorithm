import sys

def binary(N):
    result = []
    while N > 0:
        result.append(N%2)
        N //= 2
    
    return result

if __name__ == "__main__":
    
    T = int(input())
    
    for i in range(T):
        N = int(input())
        result = binary(N)
        
        flag = 1
        for i in range(len(result)):
            if result[i] == 1 and flag == 1:
                print(i, end="")
                flag = 0
            elif result[i] == 1:
                print(" {}".format(i), end="")
        print("")
        