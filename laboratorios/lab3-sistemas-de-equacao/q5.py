import numpy as np
    
n = int(input())
arrayA = [float(input()) for x in range(n**2)]
arrayb = [float(input()) for x in range(n)]
A = np.array(arrayA).reshape((n,n))
b = np.array(arrayb).reshape((n,1))


def decLU(A, b):
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

L, U = decLU(A, b)

def retroSubInferior(L, b):
    y = np.zeros((len(L), 1))
    for i in range(len(y)):
        d = L[i, i]
        n = b[i]
        for j in range(i):
            n -= L[i, j] * y[j]
        y[i] = n / d
    return y

y = retroSubInferior(L, b)

def retroSubSuperior(U, y):
    x = np.zeros((len(U), 1))
    for i in range(len(x)-1, -1, -1):
        d = U[i, i]
        n = y[i]
        for j in range(len(U)-1, i-1, -1):
            n -= U[i, j] * x[j]
        x[i] = n / d
    return x

x = retroSubSuperior(U, y)
    
soma = np.sum(L+U) + np.sum(y+x)
print(f'{soma:.1f}')
