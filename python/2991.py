if __name__ == "__main__":

    A, B, C, D = map(int, input().split())
    P, M, N = map(int, input().split())

    p_cnt, m_cnt, n_cnt = 0, 0, 0

    # P
    if 0 < P % (A + B) <= A:
        p_cnt += 1
    if 0 < P % (C + D) <= C:
        p_cnt += 1

    # M
    if 0 < M % (A + B) <= A:
        m_cnt += 1
    if 0 < M % (C + D) <= C:
        m_cnt += 1

    # N
    if 0 < N % (A + B) <= A:
        n_cnt += 1
    if 0 < N % (C + D) <= C:
        n_cnt += 1

    print(p_cnt)
    print(m_cnt)
    print(n_cnt)
