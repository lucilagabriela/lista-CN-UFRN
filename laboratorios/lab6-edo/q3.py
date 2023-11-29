import numpy as np

def PontoMedio(g, x0, y0, h, n):
    x = [x0] * (n + 1)  # Vetor para armazenar os valores de x
    y = [y0] * (n + 1)  # Vetor para armazenar os valores de y

    for i in range(n):
        slope_at_start = g(x[i], y[i])  # Slope no início do intervalo
        x_mid = x[i] + h / 2.0  # Ponto médio para x
        y_mid = y[i] + (h / 2.0) * slope_at_start  # Estimativa de y no ponto médio
        slope_at_mid = g(x_mid, y_mid)  # Slope no ponto médio
        x[i + 1] = x[i] + h  # Novo valor de x
        y[i + 1] = y[i] + h * slope_at_mid  # Estimativa de y no próximo ponto

    return y[n]

# Recebendo os valores
exp = input()
x0 = float(input())
y0 = float(input())
h = float(input())
n = int(input())
g = lambda x, y: eval(exp)

# Calculando o resultado usando o método do ponto médio
saida = PontoMedio(g, x0, y0, h, n)

# Exibindo o resultado
print(f'{saida:.3f}')