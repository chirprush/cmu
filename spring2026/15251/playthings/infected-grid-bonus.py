import numpy as np

def trop(a):
    if a <= 1:
        return 0
    return 1

tropical = np.vectorize(trop)

def mat_pow(A, n):
    result = np.identity(A.shape[0], dtype=np.int64)

    # This is wrong because even the identity doesn't work correctly
    # What to do??
    for i in range(n):
        result = result @ A
        result = tropical(result)

    return result

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

n = 3
A = np.identity(n * n, dtype=np.int64)

for x1 in range(n):
    for y1 in range(n):
        for x2 in range(n):
            for y2 in range(n):
                a = n * y1 + x1
                b = n * y2 + x2

                if dist(x1, y1, x2, y2) == 1:
                    A[a, b] = 1

print(A)
print(mat_pow(A, 1))
print(mat_pow(A, n * n))
