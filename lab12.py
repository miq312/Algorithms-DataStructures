import time

def naive_metod(S: str, W: str):
    m = 0
    N = len(W)
    M = len(S)
    comparsion = 0
    result = []

    i = 0

    while m <= M - N:
        comparsion += 1
        if S[m + i] == W[i]:
            i += 1
            if i == N:
                result.append(m)
                m += 1
                i = 0
        else:
            m += 1
            i = 0
    return result, comparsion

def hash(word, N, d = 256, q = 101):
    hw = 0
    for i in range(N):
        hw = (hw*d + ord(word[i])) % q
    return hw
  
def rabin_karp1(S: str, W: str):
    M = len(S)
    N = len(W)
    
    hW = hash(W, N)

    comparisons = 0
    result = []

    for m in range(M - N + 1):
        hS = hash(S[m:m+N], N)
        comparisons +=1
        if hS == hW:
            if S[m:m+N] == W:
                result.append(m)

    return result, comparisons

def rabin_karp2(S,W, d = 256, q = 101):
    M = len(S)
    N = len(W)
    hW = 0
    hS = 0
    h = 1
    result = []
    comparisons = 0
    collisions = 0

    for i in range(N - 1):
        h = (h * d) % q

    hW = hash(W, N)
    hS = hash(S, N)

    for m in range(M - N + 1):
        comparisons += 1
        if hW == hS:
            if S[m:m + N] == W:
                result.append(m)
            else:
                collisions += 1
        if m < M - N:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q
            if hS < 0:
                hS = hS + q
    return result, comparisons, collisions

def main():
    with open("lotr.txt", encoding='utf-8') as f:
            text = f.readlines()

    S = ' '.join(text).lower()
    W = "time."

    t_start = time.perf_counter()
    matches_naive, comparisons_naive = naive_metod(S, W)
    t_stop = time.perf_counter()
    naive_time = t_stop - t_start

    t_start = time.perf_counter()
    matches_rabin_karp1, comparisons_rabin_karp1 = rabin_karp1(S, W)
    t_stop = time.perf_counter()
    rabin_karp_time = t_stop - t_start

    t_start = time.perf_counter()
    matches_rabin_karp2, comparisons_rabin_karp2, collisions_rabin_karp2 = rabin_karp2(S, W)
    t_stop = time.perf_counter()
    rabin_karp_time = t_stop - t_start

    print(f"{len(matches_naive)};{comparisons_naive}")
    #print(f"{len(matches_rabin_karp1)};{comparisons_rabin_karp1})
    print(f"{len(matches_rabin_karp2)};{comparisons_rabin_karp2};{collisions_rabin_karp2}")

if __name__ == "__main__":
      main()