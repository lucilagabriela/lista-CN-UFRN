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

def gauss_seidel(A, b, x0, p, itMax):
    n = len(b)
    x = np.copy(x0)
    erro_rel = np.inf
    num_iteracoes = 0
    
    while erro_rel > p and num_iteracoes < itMax:
        x_antigo = np.copy(x)
        for i in range(n):
            soma = 0
            for j in range(n):
                if j != i:
                    soma += A[i][j] * x[j]
            x[i] = (b[i] - soma) / A[i][i]
        
        erro_rel = np.linalg.norm(x - x_antigo, np.inf) / np.linalg.norm(x, np.inf)
        num_iteracoes += 1
    
    return x, erro_rel, num_iteracoes

# Chamada da função
x, erro_rel, num_iteracoes = gauss_seidel(A, b, x0, p, itMax)

somaX = np.sum(x)
print(f'{somaX:.4f} {num_iteracoes} {erro_rel:.7f}')
