import numpy as np

exp = input()
x0 = float(input())
y0 = float(input())
h = float(input())
n = int(input())
g = lambda x, y: eval(exp)

def Heun(g, x0, y0, h, n):
    x = [x0]
    y = [y0]

    for i in range(n):
        xAnt = x[-1]
        yAnt = y[-1]

        k1 = g(xAnt, yAnt)
        k2 = g(xAnt + h, yAnt + h * k1)

        yNext = yAnt + 0.5 * h * (k1 + k2)
        xNext = xAnt + h

        x.append(xNext)
        y.append(yNext)

    return x, y

resultado = Heun(g, x0, y0, h, n)
xValores, yValores = resultado

saida = yValores[-1]

print(f'{saida:.3f}')