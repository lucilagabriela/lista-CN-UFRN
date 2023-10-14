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

def jacobi(A, b, p, itMax):
    B = np.zeros((len(A), len(A)))
    for i in range(len(B)):
        for j in range(len(B)):
            if i != j:
                B[i, j] = -A[i, j]/ A[i, i]
    
    d = np.zeros((len(B), 1))
    for i in range(len(d)):
        d[i] = b[i]/A[i, i]

    x = np.zeros((len(A), 1))
    erro = 1
    it = 0
    while (erro > 10**(-p)) and (i < itMax):
        x_old = np.copy(x)
        x = B@x + d
        it += 1
        erro = max(abs(x - x_old))/max(abs(x))
    return x, it, erro

x, it, erro = jacobi(A, b, p, itMax)

somaX = np.sum(x)
print(f'{somaX:.4f} {it} {erro:.7f}')