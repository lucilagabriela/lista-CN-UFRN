import numpy as np

n = int(input())
arrayA = [(
    [36, 0, -19, 0, 0],
    [0, 41, -25, 0, 0],
    [-19, -25, 88, -17, -28],
    [0, 0, -17, 35, -18],
    [0, 0, -28, -18, 60]
)]
arrayb = [(
    [206],
    [-163],
    [-217],
    [152],
    [0]
)]
#A = np.array(arrayA).reshape((n,n))
#b = np.array(arrayb).reshape((n,1))

for i in range(n):
    pivot = i
    for j in range(i + 1, n):
        if abs(A[j, i]) > abs(A[pivot, i]):
            pivot = j
    A[[i, pivot]] = A[[pivot, i]]
    b[[i, pivot]] = b[[pivot, i]]
    for j in range(i + 1, n):
        factor = A[j, i] / A[i, i]
        A[j, i:] -= factor * A[i, i:]
        b[j] -= factor * b[i]

x = np.linalg.solve(arrayA, arrayb)

somaX = np.sum(x)
print(f'{somaX:.1f}')
