import numpy as np

##   Recebe os vetores A e b do sistema
##                                          
##   Não altere o código abaixo           
##    
n = int(input())
arrayX = [float(input()) for x in range(n)]
arrayY = [float(input()) for x in range(n)]
x = np.array(arrayX).reshape((n, 1))
y = np.array(arrayY).reshape((n, 1))

x_mean = np.mean(x)
y_mean = np.mean(y)

a1 = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
a0 = y_mean - a1 * x_mean

y_pred = a0 + a1 * x
erro_quadratico = np.sum((y - y_pred) ** 2)

a = np.array([a0, a1]).reshape(-1, 1)

EQ = erro_quadratico

soma = np.sum(a) + EQ
print(f'{soma:.4f}')