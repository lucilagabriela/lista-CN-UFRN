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
        slopeInicio = g(x[i], y[i])
        x_mid = x[i] + h / 2.0
        y_mid = y[i] + (h / 2.0) * slopeInicio
        slopeNoMeio = g(x_mid, y_mid)
        x[i + 1] = x[i] + h
        y[i + 1] = y[i] + h * slopeNoMeio

    return y[n]

saida = PontoMedio(g, x0, y0, h, n)

print(f'{saida:.3f}')