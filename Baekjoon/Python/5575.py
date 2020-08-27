if __name__ == "__main__":

    for i in range(3):
        people = list(map(int, input().split()))
        pre = people[0] * 3600 + people[1] * 60 + people[2]
        post = people[3] * 3600 + people[4] * 60 + people[5]
        result = post - pre

        hour = result // 3600
        minute = (result % 3600) // 60
        second = (result % 3600) % 60
        print(hour, minute, second)



