import numpy as np

def d(n):
    A = np.ones((n, n))

    for i in range(n):
        A[i, i] = 0

    print(A)

    return np.linalg.det(A)

print([d(i) for i in range(1, 11)])
