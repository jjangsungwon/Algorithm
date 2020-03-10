from operator import itemgetter

if __name__ == "__main__":
    
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    
    money = 0
    
    data.sort(key = lambda d : d[0])
    set_min = data[0][0]
    data.sort(key = lambda d : d[1])
    unit_min = data[0][1]
         
    if N >=6:
        quotient = N // 6
        remain = N % 6
        
        result = min(remain * unit_min + quotient * set_min, (quotient+1) * set_min, N * unit_min)
    else:
        result = min(N * unit_min, set_min)
    
    print(result)