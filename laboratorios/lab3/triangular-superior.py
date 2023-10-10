import numpy as np

n = int(input())
arrayA = [float(input()) for x in range(n**2)]
arrayb = [float(input()) for x in range(n)]
A = np.array(arrayA).reshape((n,n))
b = np.array(arrayb).reshape((n,1))

x = np.zeros((n,1))
for i in range(n - 1, -1, -1):
    soma = 0
    for j in range(i + 1, n):
        soma += A[i, j] * x[j]
    x[i] = (b[i] - soma) / A[i][i]

somaX = np.sum(x)
print(f'{somaX:.1f}')