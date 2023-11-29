import numpy as np

exp = input()
x0 = float(input())
y0 = float(input())
h = float(input())
n = int(input())
g = lambda x, y: eval(exp)

def RK4(g, x0, y0, h, n):
    x = [x0]
    y = [y0]
    
    for i in range(n):
        k1 = h * g(x[i], y[i])
        k2 = h * g(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * g(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * g(x[i] + h, y[i] + k3)
        
        yi = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        xi = x[i] + h
        
        x.append(xi)
        y.append(yi)
    
    return y[-1]  # Retorna o valor de f(x_n)

saida = RK4(g, x0, y0, h, n)

print(f'{saida:.3f}')