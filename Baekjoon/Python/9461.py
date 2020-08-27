import sys

if __name__ == "__main__":
    
    T = int(sys.stdin.readline())
    
    for i in range(T):
        N = int(sys.stdin.readline())
        
        if N <=2:
            print(1)
        else:
            data_list = [0 for _ in range(N)]
            data_list[0], data_list[1], data_list[2] = 1, 1, 1

            for i in range(3, N):
                data_list[i] = data_list[i-3] + data_list[i-2]

            print(data_list[N-1])