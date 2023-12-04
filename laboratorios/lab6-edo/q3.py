import numpy as np

exp = input()
x0 = float(input())
y0 = float(input())
h = float(input())
n = int(input())
g = lambda x, y: eval(exp)

def PontoMedio(g, x0, y0, h, n):
    x = [x0] * (n + 1)
    y = [y0] * (n + 1)

    for i in range(n):
        k1 = g(x[i], y[i])
        x0 = x[i] + h / 2.0
        y0 = y[i] + (h / 2.0) * k1
        k2 = g(x0, y0)
        x[i + 1] = x[i] + h
        y[i + 1] = y[i] + h * k2

    return y[n]

saida = PontoMedio(g, x0, y0, h, n)

print(f'{saida:.3f}')