import numpy as np

a = float(input())
n = int(input()) # grau do polinomio
x = [float(input()) for x in range(n+1)]
y = [float(input()) for x in range(n+1)]

def lagrange(p, x0, y0, n):
    PdeA = 0
    for i in range(0, n+1):
        L = 1
        for j in range(0, n+1):
            if i != j:
                L *= (p-x0[j])/(x0[i]-x0[j])
    
        PdeA += y0[i]*L

    return PdeA

PdeA = lagrange(a, x, y, n)

print(f'{PdeA:.4f}')
