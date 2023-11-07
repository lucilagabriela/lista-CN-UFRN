import numpy as np

a = float(input())
n = int(input())
x = [float(input()) for x in range(n+1)]
y = [float(input()) for x in range(n+1)]

def Erro(x0, x1, x2, erro, a):
    return (erro*(a-x0)*(a-x1)*(a-x2))

def tabela(x, y):
    tamX = np.size(x)
    T = np.zeros((tamX, tamX))
    for i in range(tamX):
        T[i, 0] = y[i]
    for j in range(1, tamX):
        for i in range(tamX-j):
            T[i, j] = (T[i+1,j-1] - T[i,j-1]) / (x[i+j] - x[i])
        return T
    
def newton(x, y, n, a):
    T = tabela(x, y)
    soma = T[0, 0]
    for i in range(1, n+1):
        m = T[0, i]
        for j in range(i):
            m = m * (a-x[j])
        soma = soma + m
    return soma

T = tabela(x, y)

resultadoNewton = newton(x, y, n, a)

bn = T[0, n]
print(bn)
PdeA = resultadoNewton + bn

print(f'{PdeA:.4f}')
