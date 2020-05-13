if __name__ == "__main__":

    T = int(input())

    for i in range(T):
        num = float(input())

        # 20% 할인
        num *= 0.8
        print("$%0.2f" %num)
