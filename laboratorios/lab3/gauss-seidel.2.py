import numpy as np

p = int(input())
itMax = int(input())
n = int(input())
arrayA = [float(input()) for _ in range(n**2)]
arrayb = [float(input()) for _ in range(n)]
arrayx0 = [float(input()) for _ in range(n)]
A = np.array(arrayA).reshape((n, n))
b = np.array(arrayb).reshape((n, 1))
x0 = np.array(arrayx0).reshape((n, 1))

def gaussSeidel(A, b, x0, precisao, itMax):
    n = len(b)
    x = np.copy(x0)
    erro_relativo = np.inf
    iteracoes = 0
    
    while erro_relativo > precisao and iteracoes < itMax:
        x_antigo = np.copy(x)
        
        for i in range(n):
            soma1 = np.dot(A[i, :i], x[:i])
            soma2 = np.dot(A[i, i+1:], x_antigo[i+1:])
            x[i] = (b[i] - soma1 - soma2) / A[i, i]
        
        erro_relativo = np.linalg.norm(x - x_antigo, np.inf) / np.linalg.norm(x, np.inf)
        iteracoes += 1
    
    return x, erro_relativo, iteracoes

solucao, erro, iteracoes = gaussSeidel(A, b, x0, 10**(-p), itMax)

somaX = np.sum(solucao)

print(f'{somaX:.4f} {iteracoes} {erro:.7f}')