def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
if __name__ == "__main__":
    
    N = int(input())
    
    if N == 0:
        print(0)
    else:
        result = str(factorial(N))
    
        cnt = 0
        for i in range(len(result)-1, -1, -1):
            if result[i] == "0":
                cnt +=1
            else:
                print(cnt)
                exit()
