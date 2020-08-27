if __name__ == "__main__":

    S, K, H = map(int, input().split())

    if S + K + H >= 100:
        print("OK")
    else:
        if min(min(S, K), H) == S:
            print("Soongsil")
        elif min(min(S, K), H) == K:
            print("Korea")
        else:
            print("Hanyang")