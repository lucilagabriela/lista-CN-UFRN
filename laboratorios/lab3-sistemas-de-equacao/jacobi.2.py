import numpy as np

p = int(input())
itMax = int(input())
n = int(input())
arrayA = [float(input()) for x in range(n**2)]
arrayb = [float(input()) for x in range(n)]
arrayx0 = [float(input()) for x in range(n)]
A = np.array(arrayA).reshape((n,n))
b = np.array(arrayb).reshape((n,1))
x0 = np.array(arrayx0).reshape((n,1))

def jacobi(A, b, x0, p, itMax):
    n = len(b)
    x = np.copy(x0)
    xA = np.zeros(n)
    it = 0
    while it < itMax:
        for i in range(n):
            soma = 0
            for j in range(n):
                if j != i:
                    soma += A[i, j] * xA[j]
                x[i] = (b[i] - soma) / A[i, i]
        er = np.linalg.norm(x - xA) / np.linalg.norm(x)
        if er < p:
            break
        np.copyto(xA, x)
        it += 1
    return x, it, er

x, it, er = jacobi(A, b, x0, p, itMax)

somaX = np.sum(x)
print(f'{somaX:.4f} {it} {er:.7f}')