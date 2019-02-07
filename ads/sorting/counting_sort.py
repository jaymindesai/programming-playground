from itertools import accumulate

def counting_sort(A, k=None):
    if not k:
        k = max(A)

    C = [0]*(k+1)

    for j in A:
        C[j] += 1

    C = list(accumulate(C))

    B = [0]*(len(A)+1)

    for j in A[::-1]:
        B[C[j]] = j
        C[j] -= 1

    return B[1:]

print(counting_sort([8, 2, 4, 1, 3, 6, 5, 7, 5, 5, 4, 8, 8], 8))