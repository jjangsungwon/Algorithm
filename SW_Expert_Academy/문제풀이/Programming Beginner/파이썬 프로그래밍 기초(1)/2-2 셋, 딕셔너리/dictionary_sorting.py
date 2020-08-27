# dictionary data 내림차순 정렬

import operator # key 또는 value를 기준으로 정렬하기 위해서 사용

# dictionary data
dic = {"TV": 2000000, "냉장고": 1500000, "책상": 350000, "노트북": 1200000, "가스레인지": 200000, "세탁기": 1000000}

# operator.itemgettor사용(itemgettor(0) - 키를 기준, itemgettor(1) - 값을 기준)
# sorted 기본값이 오름차순이기때문에 내림차순을 하기위해서 reverse == True 필요.
dic = dict(sorted(dic.items(), key = operator.itemgetter(1), reverse=True))

for key, value in dic.items():
    print("{0}: {1}".format(key, value))
