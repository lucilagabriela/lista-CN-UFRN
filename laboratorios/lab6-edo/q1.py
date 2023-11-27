import numpy as np

exp = input()
x0 = float(input())
y0 = float(input())
h = float(input())
n = int(input())
g = lambda x, y: eval(exp)

def euler(g, x0, y0, h, n):
    x = [x0]
    y = [y0]

    for i in range(n):
        yNext = y[-1] + h * g(x[-1], y[-1])
        xNext = x[-1] + h
        x.append(xNext)
        y.append(yNext)

    return y[-1]


saida = euler(g, x0, y0, h, n)

print(f'{saida:.3f}')