import sys

if __name__ == "__main__":
    N = int(input())
    f = "* "
    s = " *"
    
    if N == 1:
        print("*")
    else:
        for i in range(N):
            for j in range(N):
                if j == N - 1:
                    if i % 2 == 0:
                        print("*")
                    else:
                        print(" *")
                else:
                    if i % 2 == 0:
                        print(f,end="")
                    else:
                        print(s,end="")
               
