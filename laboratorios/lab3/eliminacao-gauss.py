import numpy as np

n = int(input())
arrayA = [float(input()) for x in range(n**2)]
arrayb = [float(input()) for x in range(n)]
A = np.array(arrayA).reshape((n,n))
b = np.array(arrayb).reshape((n,1))

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

x = np.linalg.solve(A, b)

somaX = np.sum(x)
print(f'{somaX:.1f}')
