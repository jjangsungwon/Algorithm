if __name__ == "__main__":

    pre_temperature = float(input())
    while pre_temperature != 999:
        post_temperature = float(input())

        if post_temperature == 999:
            break
        else:
            print("%.2f" %(post_temperature - pre_temperature))
            pre_temperature = post_temperature
