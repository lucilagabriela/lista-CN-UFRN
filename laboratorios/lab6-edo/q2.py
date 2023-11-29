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
        xPrev = x[-1]
        yPrev = y[-1]

        k1 = g(xPrev, yPrev)
        k2 = g(xPrev + h, yPrev + h * k1)

        yNext = yPrev + 0.5 * h * (k1 + k2)
        xNext = xPrev + h

        x.append(xNext)
        y.append(yNext)

    return x, y

# Chamando a função Heun
resultado = Heun(g, x0, y0, h, n)
xValores, yValores = resultado

# Valor de f(x_n) após n iterações
saida = yValores[-1]

# Saída formatada
print(f'{saida:.3f}')