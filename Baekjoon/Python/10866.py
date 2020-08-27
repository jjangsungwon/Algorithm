import sys

if __name__ == "__main__":
    N = int(input())
    
    Deque = []
    for i in range(N):
        order = sys.stdin.readline().split()

        if order[0] == "push_back":
            Deque.append(order[1])
        elif order[0] == "push_front":
            Deque.insert(0, order[1])
        elif order[0] == "pop_front":
            if len(Deque) == 0:
                print(-1)
            else:
                print(Deque[0])
                Deque.pop(0)
        elif order[0] == "pop_back":
            if len(Deque) == 0:
                print(-1)
            else:
                print(Deque[-1])
                Deque.pop(-1)
        elif order[0] == "size":
            print(len(Deque))
        elif order[0] == "front":
            if len(Deque) == 0:
                print(-1)
            else:
                print(Deque[0])
        elif order[0] == "back":
            if len(Deque) == 0:
                print(-1)
            else:
                print(Deque[-1])
        elif order[0] == "empty":
            if len(Deque) == 0:
                print(1)
            else:
                print(0)
    