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

def metodoJacobi(A, b, x0, precisao, itMax):
    n = len(b)
    x = np.copy(x0)
    erro_relativo = np.inf
    iteracoes = 0
    
    while erro_relativo > precisao and iteracoes < itMax:
        x_antigo = np.copy(x)
        
        for i in range(n):
            soma = 0
            for j in range(n):
                if j != i:
                    soma += A[i][j] * x_antigo[j]
            x[i] = (b[i] - soma) / A[i][i]
        
        erro_relativo = np.linalg.norm(x - x_antigo, np.inf) / np.linalg.norm(x, np.inf)
        iteracoes += 1
    
    return x, erro_relativo, iteracoes

solucao, erro, iteracoes = metodoJacobi(A, b, x0, 10**(-p), itMax)

somaX = np.sum(solucao)

print(f'{somaX:.4f} {iteracoes} {erro:.7f}')