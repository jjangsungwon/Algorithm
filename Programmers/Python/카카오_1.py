import math
from numpy.linalg import norm
from numpy import dot
import numpy as np

word_dic = {}
key_list = []


def cos_sim(A, B):
    A_temp = []
    B_temp = []
    for i in range(len(A)):
        A_temp.append(A[i][0])
    for i in range(len(B)):
        B_temp.append(B[i][0])

    # key_list에 해당하는 각각의 값으로 새로운 배열 생성
    A_list = []
    B_list = []

    for key in key_list:
        # A
        if key in A_temp:
            index = A_temp.index(key)
            A_list.append(A[index][1])
        else:
            A_list.append(0)

        # B
        if key in B_temp:
            index = B_temp.index(key)
            B_list.append(B[index][1])
        else:
            B_list.append(0)

    return dot(A_list, B_list) / (norm(A_list) * norm(B_list))


def f(t, d):  # 문서 d에서 t가 나오는 횟수
    return d.count(t)


def tf(t, d):
    return 0.5 + 0.5 * f(t, d) / max([f(w, d) for w in d])


def idf(t, D):
    count = 0
    for key in D.keys():
        if t in D[key]:
            count += 1
    return math.log(N / count)


def tfidf(t, d, D):
    return tf(t, d) * idf(t, D)


if __name__ == "__main__":
    # inputs
    N = int(input())  # 뉴스 정보의 수
    key_value = []
    for _ in range(N):
        DOC_ID, W = map(int, input().split())  # id, 개수
        word = list(map(str, input().split()))
        key_list.extend(word)
        word_dic[DOC_ID] = word
        key_value.append(str(DOC_ID))
    # tf-idf 계산
    result = []
    for key in word_dic.keys():
        result.append([(t, tfidf(t, word_dic[key], word_dic)) for t in word_dic[key]])

    # 중복 제거
    key_list = list(set(key_list))

    Clustering = {}
    # 문서 유사도 계산 ( 코사인 유사도) 및 클러스터링
    flag, cluster_flag, index = False, False, 0
    for key in word_dic.keys():
        cluster_flag = False
        if not flag:  # 제일 처음값 초기화
            Clustering[key] = 1
            flag = True
        else:
            for temp_key in Clustering:  # 클러스트링에 있는 값과 유사도 비교
                Clustering_index = key_value.index(str(temp_key))
                cos_sim_value = cos_sim(result[Clustering_index], result[index])
                if cos_sim_value >= 0.98:
                    Clustering[temp_key] += 1
                    cluster_flag = True
            if not cluster_flag:
                Clustering[key] = 1
        index += 1

    print(len(Clustering))  # 총 갯수
    for key in Clustering:
        print(key, Clustering[key])
