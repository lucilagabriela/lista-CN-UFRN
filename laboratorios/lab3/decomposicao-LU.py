import numpy as np

n = int(input())
arrayA = [float(input()) for x in range(n**2)]
arrayb = [float(input()) for x in range(n)]
A = np.array(arrayA).reshape((n,n))
b = np.array(arrayb).reshape((n,1))


""""
for j in range (1, n - 1):
    pivor = A[j, j]
    for i in range (j + 1, n):
        fator = A[i, j] / pivor
        A[i, :] = A[i, :] - fator * A[j, :]
        L[i, j] = fator
"""

def fatoraLU(A):  
    U = np.copy(A)  
    n = np.shape(U)[0]  
    L = np.eye(n)  
    for j in np.arange(n-1):  
        for i in np.arange(j+1,n):  
            L[i,j] = U[i,j]/U[j,j]  
            for k in np.arange(j+1,n):  
                U[i,k] = U[i,k] - L[i,j]*U[j,k]  
            U[i,j] = 0  
    return L, U

L, U = fatoraLU(A)

somaX = np.sum(L+U)
print(f'{somaX:.1f}')