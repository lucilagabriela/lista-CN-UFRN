import numpy as np

n = int(input())
arrayA = [float(input()) for x in range(n**2)]
arrayb = [float(input()) for x in range(n)]
A = np.array(arrayA).reshape((n,n))
b = np.array(arrayb).reshape((n,1))

def decLU(A, b):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    y = np.zeros((n, 1))
    x = np.zeros((n, 1))
    for i in range(n):
        L[i, i] = 1
        for j in range(i, n):
            soma = 0
            for k in range(i):
                soma += L[i, k] * U[k, j]
            U[i, j] = A[i, j] - soma
        
        for j in range(i+1, n):
            soma = 0
            for k in range(i):
                soma += L[j, k] * U[k, i]
            
            L[j, i] = (A[j, i] - soma)/U[i, i]
    
    for i in range(n):
        soma = 0
        for j in range(i):
            soma += L[i, j] * y[j]
        y[i] = b[i] - soma
    
    for i in range(n-1, -1, -1):
        soma = 0
        for j in range(i+1, n):
            soma += U[i, j] * x[j]
        x[i] = (y[i] - soma) / U[i, i]
    
    return L, U, y, x

L, U, y, x = decLU(A, b)

soma = np.sum(L+U) + np.sum(y+x)
print(f'{soma:.1f}')
